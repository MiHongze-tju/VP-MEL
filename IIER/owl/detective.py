import torch
from transformers import AutoModel
from models.configuration_mplugowl3 import mPLUGOwl3Config
from models.modeling_mplugowl3 import mPLUGOwl3Model
import os
import re
import os
import time
import json

model_path = './models'
config = mPLUGOwl3Config.from_pretrained(model_path)
# print(config)
# model = mPLUGOwl3Model(config).cuda().half()
model = mPLUGOwl3Model.from_pretrained(model_path, attn_implementation='sdpa', torch_dtype=torch.half)
model.eval().cuda()

from PIL import Image

from transformers import AutoTokenizer, AutoProcessor
from decord import VideoReader, cpu  # pip install decord

model_path = './models'
tokenizer = AutoTokenizer.from_pretrained(model_path)
processor = model.init_processor(tokenizer)


image_path = '' #
filenames = os.listdir(image_path)

def _load_json_file(filepath):
    data = []
    if isinstance(filepath, str):
        with open(filepath, 'r', encoding='utf-8') as f:
            d = json.load(f)
            data.extend(d)
    elif isinstance(filepath, list):
        for path in filepath:
            with open(path, 'r', encoding='utf-8') as f:
                d = json.load(f)
                data.extend(d)
    return data


def entity_(path):
    with open(path,'r',encoding='utf-8') as f:
        L = f.readlines()

    entityDict = [[] for i in range(len(L))]


    print('L',len(L))
    for i in range(0, len(L)):
        id = i
        key = re.findall(r'^(.*?)###', L[i])[0]
        value = re.findall(r'###(.*?)\n', L[i])
        entityDict[id].append(key)
        entityDict[id].append(value)



    return entityDict

entityDict = entity_('')
testData = _load_json_file('')

for i in range(len(testData)):
    img_set = []
    image = Image.open(os.path.join(image_path, testData[i]['imgPath']))
    img_set.append(image)

    sentence = testData[i]['sentence']
    id = testData[i]['id']

    messages = [
        {"role": "user", "content": f"""<|image|> 
        In the red box of the image, tell me briefly what is the Entity Type, and which Entity Name in the <|sentence|> corresponds to the Entity Type ? """},
        {"role": "assistant", "content": ""}
    ]

    inputs = processor(messages, images=img_set, videos=None)


    inputs.to('cuda')
    inputs.update({
        'tokenizer': tokenizer,
        'max_new_tokens': 100,
        'decode_text': True,
    })

    g = model.generate(**inputs)

    with open("/dataset/owl-answers.txt", "a", encoding='utf-8') as file:
        file.write('imgid:' + id + '###' + g[0] + '\n')
    print(imgid, '    finished')

