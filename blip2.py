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

img_path = './image.jpg' # Path to the image file
raw_image = Image.open(img_path).convert('RGB')
raw_image.resize((596, 437))