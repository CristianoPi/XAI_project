#BLOCCO UTILE SOLO AD ADATTARE VECCHIA STRUTTURA DELLA CARTELLA ALLA NUOVA

import csv, re, shutil
from pathlib import Path

SRC_ROOT = Path("dataset_1/images")      # cartelle esistenti
DEST_ROOT = Path("dataset")                         # nuova struttura
IMG_DIR   = DEST_ROOT / "images"; IMG_DIR.mkdir(parents=True, exist_ok=True)
META_CSV  = DEST_ROOT / "dataset_metadata.csv"

objects = [
    "ceramic coffee mug", 
    "book jacket",
    "soft couch pillow", 
    "opaque metal water bottle",
    "table lamp with shade (off)", 
    "granny smith", 
    "notebook with kraft cover"
]

contexts = [
    "plain white studio background", 
    "minimalist living-room corner",
    "modern office desk", 
    "kitchen countertop daylight",
    "green park lawn afternoon light", 
    "science lab bench",
    "garage workshop tools on pegboard", 
    "hotel room desk area",
    "bathroom vanity matte tiles", 
    "classroom row of desks daylight"
]

prompt_map = {
    f"{obj.replace(' ', '_').lower()}__{ctx.replace(' ', '_').replace('/', '_').lower()}":
    f"A neutral {obj} in a {ctx} background"
    for obj in objects
    for ctx in contexts
}

def normalize(name: str) -> str:
    n = name.lower().replace("/", "_").replace(" ", "_")
    n = re.sub(r"__+", "__", n).strip("_")
    return n

def build_filename(obj_ctx: str, idx: int) -> str:
    obj_part, ctx_part = obj_ctx.split("__", 1)
    return f"{obj_part}__{ctx_part}__{idx:03}.png"

rows = []
for folder in sorted(SRC_ROOT.iterdir()):
    if not folder.is_dir():
        continue
    key = normalize(folder.name)
    prompt = prompt_map.get(key)
    if prompt is None:
        print(f"⚠️  Skip un-recognised folder: {folder.name}")
        continue

    for i, img_path in enumerate(sorted(folder.glob("*.png")), start=1):
        new_name = build_filename(key, i)
        shutil.copy(img_path, IMG_DIR / new_name)

        seed = re.search(r"(\d+)", img_path.stem)
        rows.append({
            "file_name": f"images/{new_name}",
            "prompt": prompt,
            "seed": int(seed.group(1)) if seed else "",
            "background": key
        })

print(f"✅ Copied {len(rows)} images to {IMG_DIR}")

with META_CSV.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file_name","prompt","seed","background"])
    writer.writeheader(); writer.writerows(rows)

print("✅ metadata.csv written →", META_CSV)