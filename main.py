from flask import Flask, request, jsonify
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

app = Flask(__name__)

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/analyze', methods=["POST"])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = Image.open(request.files['image']).convert('RGB')
    
    inputs = processor(image, return_tensors="pt")
    
    with torch.no_grad():
        out = model.generate(**inputs)
        
    result = processor.decode(out[0], skip_special_tokens=True)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)