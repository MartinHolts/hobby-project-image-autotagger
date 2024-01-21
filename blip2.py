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

# setup device to use CPU
device = "cpu"

# 2.7 Coco
model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=device
)

vis_processors.keys()