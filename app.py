from flask import Flask, request, render_template
import timm
import torch
from torchvision import transforms
from PIL import Image
import os
import sys

model = timm.create_model('vit_tiny_patch16_224.augreg_in21k_ft_in1k', pretrained=False, num_classes=102)
model.load_state_dict(torch.load("trained_flower_classification_model.pth", weights_only=True))
model.eval()

sys.path.append('.') 
from labels import labels

app = Flask(__name__)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.route('/')
def index():
    return render_template('index.html', classification=None, confidence=None, image_url=None)

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files or request.files['file'].filename == '':
        return render_template('index.html', classification="No file uploaded", confidence=None, image_url=None)

    file = request.files['file']
    image = Image.open(file.stream).convert('RGB')

    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)
    
    contents = os.listdir(upload_folder)
    for item in contents:
        item_path = os.path.join(upload_folder, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        
    image_path = os.path.join(upload_folder, file.filename)
    image.save(image_path)

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence, predicted_idx = torch.max(probabilities, dim=0)

    predicted_class_id = predicted_idx.item() + 1
    predicted_class = labels.get(predicted_class_id, "Unknown")

    return render_template(
        'index.html', 
        classification=predicted_class, 
        confidence=f"{confidence.item():.2f}", 
        image_url=f"/{image_path}" 
    )

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV', 'development')

    if env == 'production':
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='127.0.0.1', port=5000, debug=True)
