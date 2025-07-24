import csv
import re
from pathlib import Path

# Percorsi
IMG_DIR = Path("dataset_1/images")  # Directory contenente le immagini
META_CSV = Path("dataset_metadata.csv")  # File CSV da generare

# Funzione per estrarre informazioni dal nome del file
def parse_filename(filename):
    # Esempio: "bookjacket__classroom__001.png"
    match = re.match(r"(?P<object>.*?)__(?P<context>.*?)__(?P<index>\d+)\.png", filename)
    if match:
        return match.group("object"), match.group("context"), int(match.group("index"))
    return None, None, None

# Creazione del dataset_metadata.csv
rows = []
for img_path in sorted(IMG_DIR.glob("*.png")):
    object_name, context_name, index = parse_filename(img_path.name)
    if object_name and context_name:
        prompt = f"A neutral {object_name.replace('_', ' ')} in a {context_name.replace('_', ' ')} background"
        rows.append({
            "file_name": f"images/{img_path.name}",
            "prompt": prompt,
            "object": object_name.replace('_', ' '),
            "background": context_name.replace('_', ' ')
        })

# Scrittura del file CSV
with META_CSV.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["file_name", "prompt", "object", "background"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ metadata.csv written → {META_CSV}")