#Take pictures from diffusiondb, this solution is not aviable for our use case
import os, pandas as pd, urllib.request, zipfile, csv
from pathlib import Path
from PIL import Image
from tqdm.auto import tqdm
import numpy as np
import openai
from numpy.linalg import norm

# --- configuration ---
openai.api_key = os.getenv("OPENAI_API_KEY")

OBJ_CTX_PAIRS = [("apple", "studio")]
CLIP_THRESH = 0.30
COSINE_THRESH = 0.30
MAX_IMAGES = 50
MAX_PARTS = 5

BASE = Path("./dataset_diffdb")
IMG_DIR = BASE / "images"; IMG_DIR.mkdir(parents=True, exist_ok=True)
CSV_META = BASE / "dataset_metadata.csv"
META_URL = "https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/metadata.parquet"
META_FILE = BASE / "metadata.parquet"


def make_prompt(obj, ctx):
    return (
        f"A product shot photo of a red {obj}, close-up, "
        f"on a clean {ctx} background, soft natural lighting, minimalistic composition"
    )

# --- download metadata.parquet if needed ---
if not META_FILE.exists():
    print("⬇️ Downloading metadata.parquet…")
    urllib.request.urlretrieve(META_URL, META_FILE)

# --- Load metadata and filter by object/context presence + CLIP ---
cols = ["image_name", "prompt", "part_id", "cfg", "seed", "clip", "sampler"]
df = pd.read_parquet(META_FILE, columns=cols)
df["prompt"] = df.prompt.str.lower()

# Apply text filter
mask = df.prompt.apply(lambda t: any(o in t and ctx in t for o, ctx in OBJ_CTX_PAIRS)) & (df.clip >= CLIP_THRESH)
df_f = df[mask].reset_index(drop=True)

# Limit by number of parts and images
parts = df_f.part_id.unique().tolist()[:MAX_PARTS]
df_f = df_f[df_f.part_id.isin(parts)].head(MAX_IMAGES).reset_index(drop=True)

# Embedding of prompts
print("🔍 Calcolo embedding dei prompt con OpenAI")
prompt_map = {make_prompt(o, c): (o, c) for o, c in OBJ_CTX_PAIRS}
prompt_embeds = {p: np.array(openai.Embeddings.create(model="text-embedding-3-small", input=p).data[0].embedding)
                 for p in prompt_map.keys()}

#  Download images and compare embeddings 
to_keep = []
parts_done = set()

for _, r in tqdm(df_f.iterrows(), total=len(df_f), desc="Verifica embedding"):
    # Trova il prompt strutturato associato a questo record
    matched = next((p for p, (o, c) in prompt_map.items() if o in r.prompt and c in r.prompt), None)
    if matched is None:
        continue

    # Download part.zip if needed
    if r.part_id not in parts_done:
        zip_n = f"part-{int(r.part_id):06}.zip"
        urllib.request.urlretrieve(f"https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/images/{zip_n}", zip_n)
        zipfile.ZipFile(zip_n).extractall(f"part-{int(r.part_id):06}")
        parts_done.add(r.part_id)

    # Image embedding
    img = Image.open(Path(f"part-{int(r.part_id):06}") / r.image_name)
    img_bytes = open(img.fp.name, "rb").read()
    resp = openai.Embeddings.create(model="text-embedding-ada-002", input=img_bytes)
    img_emb = np.array(resp.data[0].embedding)

    # Cosine similarity
    cosine = np.dot(prompt_embeds[matched], img_emb) / (norm(prompt_embeds[matched]) * norm(img_emb))
    if cosine >= COSINE_THRESH:
        r["prompt_structured"] = matched
        r["cosine"] = cosine
        to_keep.append(r)

df_sel = pd.DataFrame(to_keep)

# --- Save selected images and CSV ---
with open(CSV_META, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file", "prompt", "prompt_structured", "cfg", "seed", "sampler", "clip", "cosine"])
    writer.writeheader()
    for _, r in df_sel.iterrows():
        src = Path(f"part-{int(r.part_id):06}") / r.image_name
        Image.open(src).save(IMG_DIR / r.image_name)
        writer.writerow({
            "file": f"images/{r.image_name}",
            "prompt": r.prompt,
            "prompt_structured": r.prompt_structured,
            "cfg": float(r.cfg),
            "seed": int(r.seed),
            "sampler": int(r.sampler),
            "clip": float(r.clip),
            "cosine": round(float(r.cosine), 4)
        })

print("✅ Dataset finale creato:", len(df_sel), "immagini.")