from flask import Flask, request, jsonify
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForQuestionAnswering

app = Flask(__name__)

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

@app.route('/qna', methods=["POST"])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = Image.open(request.files['image']).convert('RGB')
    prompt = request.form.get('prompt', 'What is in the image?')
    
    inputs = processor(image, prompt, return_tensors="pt")
    
    with torch.no_grad():
        out = model.generate(**inputs)
        
    result = processor.decode(out[0], skip_special_tokens=True)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)