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

# we associate a model with its preprocessors to make it easier for inference.

# COCO
# 2.7 Coco
# Tried. Ran 4 minutes. Couldn't generate great tags.
#model, vis_processors, _ = load_model_and_preprocess(
#    name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=device
#)
# 6.7 Coco
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="caption_coco_opt6.7b", is_eval=True, device=device
# )
# 5XL Coco
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_t5", model_type="caption_coco_flant5xl", is_eval=True, device=device
# )

# PRETRAIN
# 2.7B Pretrain
# Tried. Ran 4 minutes. Generated longer caption than Coco. Didn't generate tags.
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="pretrain_opt2.7b", is_eval=True, device=device
# )
# 6.7B Pretrain
# TRIED. Ran 4 hours.
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_opt", model_type="pretrain_opt6.7b", is_eval=True, device=device
# )
# 5XL Pretrain
# TRIED. Ran 10 minutes. Maybe faster on patch of images. Since runs checkpoints shards every time. Generated terrible captions.
# model, vis_processors, _ = load_model_and_preprocess(
#    name="blip2_t5", model_type="pretrain_flant5xl", is_eval=True, device=device
# )
# 5XXL Pretrain
# TRIED. Didn't run
# model, vis_processors, _ = load_model_and_preprocess(
#     name="blip2_t5", model_type="pretrain_flant5xxl", is_eval=True, device=device
# )

vis_processors.keys()

# Prepare the image as model input using the associated processors
image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
print("Prepared image for model")

# Generate caption using beam search
caption = model.generate({"image": image})
print(caption)

# Generate tags
tags = model.generate({"image": image, "prompt": "Question: What words describe this image?"})
print(tags)