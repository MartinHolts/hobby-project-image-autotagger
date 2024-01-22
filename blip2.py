import pkg_resources
import subprocess
import sys

try:
    pkg_resources.get_distribution('salesforce-lavis')
    print("salesforce-lavis is installed.")
except pkg_resources.DistributionNotFound:
    print("Installing salesforce-lavis...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "salesforce-lavis"])


import torch
from PIL import Image
import requests
from lavis.models import load_model_and_preprocess

# Import image file and convert to RGB and resize
img_path = './image.jpg'
raw_image = Image.open(img_path).convert('RGB')
raw_image.resize((596, 437))

# Setup device to use CPU
device = "cpu"

""" Load pretrained/finetuned BLIP2 captioning model
 2.7 Coco
model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=device
)"""

# Load pretrained/finetuned BLIP2 captioning model
# 2.7B Pretrain
model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_opt", model_type="pretrain_opt2.7b", is_eval=True, device=device
)
print("Loaded normal 2.7b model into RAM")

vis_processors.keys()

# Prepare the image as model input using the associated processors
image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
print("Prepared image for model")

# Generate caption using beam search
caption = model.generate({"image": image})
print(caption)

# Generate tags
tags = model.generate({"image": image, "prompt": "Generate 20 tags for this image, separated by commas."})
print(tags)

tags2 = model.generate({"image": image, "prompt": "Question: which city is this? Answer:"})
print(tags2)

tags3 = model.generate({"image": image, "prompt": "Describe the image."})
print(tags3)