import torch
from transformers import AutoModel
from models.configuration_mplugowl3 import mPLUGOwl3Config
from models.modeling_mplugowl3 import mPLUGOwl3Model
import os

image_path = '/home/NewHDD4090/MEL/MIMIC/dataset/WikiDiverse/mention_image'
filenames = os.listdir(image_path)
g = 'nihao'

# file = open('owl-wiki-caption.txt', 'w')
# for filename in filenames:
#     imgid = filename[8:-4]
#     file.write('imgid:' + imgid + '###' + g + '/n')
# file.close()

print(type(g))
with open("owl-wiki-caption.txt","w",encoding='utf-8') as file:
    for filename in filenames:
        imgid = filename[8:-4]
        file.write('imgid:' + imgid + '###' + g + '\n')