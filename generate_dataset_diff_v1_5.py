#execute in a Kaggle environment or in an environment with GPU where Diffusers and Torch are installed
import os
import re
import csv
import zipfile
from pathlib import Path
import torch
from tqdm.auto import tqdm
from diffusers import StableDiffusionPipeline

# --- Configuration ---
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

# --- Output Directory ---
base_dir = Path("/kaggle/working/dataset")
img_dir = base_dir / "images"
img_dir.mkdir(parents=True, exist_ok=True)
csv_meta = base_dir / "dataset_metadata.csv"

# --- Initialize Stable Diffusion Pipeline ---
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True,
    low_cpu_mem_usage=True
).to("cuda")
pipe.enable_attention_slicing()

# --- CSV setup ---
csvfile = open(csv_meta, "w", newline="")
writer = csv.DictWriter(csvfile, fieldnames=["file_name", "prompt", "object", "background"])
writer.writeheader()

# --- Generation images + metadata ---
img_counter = 1
for obj in objects:
    for ctx in contexts:
        prompt = f"A neutral {obj} in a {ctx} background"
        obj_short = obj.replace(" ", "").replace("(", "").replace(")", "").lower()
        ctx_short = ctx.split()[0].lower()  # solo la prima parola del contesto

        for i in range(5):  # Numero immagini per combinazione
            filename = f"{obj_short}__{ctx_short}__{i+1:03}.png"
            file_path = img_dir / filename

            # Generazione immagine
            img = pipe(prompt, num_inference_steps=30, guidance_scale=11).images[0]
            img.save(file_path)

            # Scrittura riga CSV
            writer.writerow({
                "file_name": f"images/{filename}",
                "prompt": prompt,
                "object": obj,
                "background": ctx
            })
            img_counter += 1

csvfile.close()
print("✅ Immagini e metadati generati!")

# --- create final ZIP ---
zip_path = "/kaggle/working/dataset.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file_path in base_dir.rglob("*"):
        zipf.write(file_path, arcname=file_path.relative_to(base_dir.parent))

print("✅ ZIP pronto per il download:", zip_path)