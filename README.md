# VisionTalk API  API

This project provides two simple Flask APIs for Vision-Language tasks using Hugging Face's BLIP models. It includes endpoints for **Image Captioning** and **Visual Question Answering (VQA)**.

## Features

- **Image Captioning (`main.py`)**: Automatically generates a descriptive caption for a given uploaded image.
- **Visual Question Answering (`qna.py`)**: Answers specific text-based questions concerning the uploaded image.

## Requirements

Make sure you have Python installed (preferably 3.8+). The required libraries are:
- `Flask`
- `Pillow`
- `torch`
- `transformers`

## Installation

1. Clone this repository or navigate to your project directory.
2. Install the necessary dependencies using pip:

```bash
pip install flask pillow torch torchvision transformers
```


## Usage

### 1. Image Captioning API (`main.py`)

This script runs a Flask server that accesses the BLIP Image Captioning base model.

**Start the server:**
```bash
python /main.py
```
*(Runs on `http://127.0.0.1:5000/` by default)*

**Endpoint Details:**
- **URL**: `http://127.0.0.1:5000/analyze`
- **Method**: `POST`
- **Payload**:
  - `image`: The image file you want to caption (multipart/form-data).

**Example cURL request:**
```bash
curl -X POST -F "image=@path_to_your_image.jpg" http://127.0.0.1:5000/analyze
```

### 2. Visual Question Answering API (`qna.py`)

This script runs a Flask server that accesses the BLIP VQA base model to answer questions about images.

**Start the server:**
```bash
python /qna.py
```
*(Runs on `http://127.0.0.1:5000/` by default)*

**Endpoint Details:**
- **URL**: `http://127.0.0.1:5000/qna`
- **Method**: `POST`
- **Payload**:
  - `image`: The image file you want to analyze (multipart/form-data).
  - `prompt`: The question you want to ask about the image (multipart/form-data text). If not provided, defaults to *"What is in the image?"*.

**Example cURL request:**
```bash
curl -X POST -F "image=@path_to_your_image.jpg" -F "prompt=What color is the car?" http://127.0.0.1:5000/qna
```

## Models Used

- [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base)
