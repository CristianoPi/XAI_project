import json
import random
import requests
import pandas as pd
from pathlib import Path
from tqdm import tqdm
from pycocotools.coco import COCO
from PIL import Image

# --- CONFIGURAZIONE ---
BASE = Path("./dataset_coco")
ANNOT_DIR = Path("./annotations")
ANNOT_FILE = ANNOT_DIR / "captions_val2017.json"
IMG_DIR = BASE / "images"; IMG_DIR.mkdir(parents=True, exist_ok=True)
CSV_META = BASE / "dataset_metadata.csv"

# Controlla presenza file JSON
if not ANNOT_FILE.exists():
    raise FileNotFoundError(f"File annotazioni mancante: {ANNOT_FILE}")

# Carica annotazioni COCO
coco = COCO(str(ANNOT_FILE))

# Seleziona 50 immagini casuali
img_ids = coco.getImgIds()
sel_ids = random.sample(img_ids, 50)

rows = []
for img_id in tqdm(sel_ids, desc="Scarico immagini"):
    info = coco.loadImgs(img_id)[0]
    url = info["coco_url"]
    fname = info["file_name"]

    # Scarica l'immagine
    resp = requests.get(url, timeout=10)
    img_path = IMG_DIR / fname
    img_path.write_bytes(resp.content)

    # Carica didascalie
    ann_ids = coco.getAnnIds(imgIds=[img_id])
    anns = coco.loadAnns(ann_ids)
    captions = [ann["caption"] for ann in anns]
    prompt = captions[0] if captions else ""

    rows.append({
        "file": f"images/{fname}",
        "prompt": prompt
    })

# Salva CSV finale
pd.DataFrame(rows).to_csv(CSV_META, index=False, encoding="utf-8")
print(f"✅ Fatto! 50 immagini salvate in {IMG_DIR} e metadata in {CSV_META}")