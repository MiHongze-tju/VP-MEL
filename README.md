<div align="center">

<h1>VP-MEL: Visual Prompts Guided Multimodal Entity Linking</h1>
</div>

<br>

<div align="center">
<img src='head.jpg' width='70%'>
</div>

# VP-MEL

# Todo List⏳

 - [ ] Release datasets and training and inference scripts.
 - [x] Release complete code for the FBMEL model.
 - [ ] Release new VPWiki dataset.

# VPWiki Dataset
</div>

<br>

<div align="center">
<img src="dataexample.jpg" width="50%">
</div>

Our VPWiki dataset is built on two benchmark MEL datasets [WikiDiverse](https://aclanthology.org/2022.acl-long.328) and [WikiMEL](https://doi.org/10.1145/3477495.3531867):

The above figure shows an example from VPWiki and WikiDiverse. The red box in the left image represents the visual prompt annotated for the VP-MEL task. The red text in the right image shows the annotated mention words.

</div>

<br>

<div align="center">
<img src="vpwikiet.png" width="25%">
</div>

We provide some sample data [here](dataset/VPWiki/test.json), and some of the corresponding images can be found in the [folder](dataset/VPWiki/test_img(Example)/).  The complete dataset will be released in subsequent updates.

# Usage

### Step 1: Set up the environment

```bash
conda create -n vpmel 
conda activate vpmel
```

Please install the specified versions of Python libraries according to the [requirements.txt](requirements.txt) file.

Note that the versions of PyTorch, Transformers, and PyTorch Lightning may have a slight impact on the results.

### Step 2: Download the data
You may download WikiMEL and RichpediaMEL from https://github.com/seukgcode/MELBench and WikiDiverse from https://github.com/wangxw5/wikiDiverse.

For our VPWiki dataset, we provide test samples for reference in the [folder](dataset/VPWiki/), and the complete dataset will be released later.

Please name the data folders according to their respective names and place them in the **dataset/** directory.

### Step 3: Instruction fine-tune the VLM
Instruction fine-tuning of VLMs can involve selecting different models based on specific requirements. In this work, we choose [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl/tree/main).

Please refer to the [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl/tree/main), download the complete model, and place it in **FBMEL/owl/**. The inference results of the VLM are incorporated as additional textual information in the training process.

We provide a prompt [template](FBMEL/owl/detective.py); however, you can adjust it according to your needs.

### Step 4: Start the training
Please update the [config](config/) file according to your file paths.

Now you can execute `bash run.sh <gpu_id> <dataset_name>` to begin the training.
```bash
bash run.sh 0 vpwiki
```

## Code Structure
The code is organized as follows:
```text
├── FBMEL
│   ├── main.py
│   ├── model
│   │   ├── lightning.py
│   │   └── modeling.py
│   ├── utils
│   │   ├── dataset.py
│   │   └── functions.py
│   └── owl
│       └── detective.py
├── config
│   └── vpwiki.yaml
├── readme.md
├── requirements.txt
└── run.sh
```

