import streamlit as st
from PIL import Image
import os
import torch
from labels import labels
import timm
from torchvision import transforms
import sys

sys.path.append('.') 

# Import the model of the NN
model = timm.create_model('vit_tiny_patch16_224.augreg_in21k_ft_in1k', pretrained=False, num_classes=102)
model.load_state_dict(torch.load("trained_flower_classification_model.pth", weights_only=True))
model.eval()

# Picture traitement before feeding the model
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Create the look of the application
st.set_page_config(page_title="FlowerFinder", page_icon="static/src/logo.jpeg")
st.title('FlowerFinder')
st.logo("static/src/logo.jpeg")

uploaded_file = st.file_uploader("Chose a picture", type=["png", "jpg", "jpeg"])
camera_file = st.camera_input("Take a photo")

if (uploaded_file is not None) :
    file = uploaded_file
elif(camera_file is not None):
    file = camera_file
if (uploaded_file is None and camera_file is None):
    file = None

@st.dialog("Get your result !!!")
def submited():
    
    # The user selected a file
    if file is None:
        st.write("Please select a picture")
    else :

        image = Image.open(file).convert('RGB')
        input_tensor = transform(image).unsqueeze(0)

        # Get the top k prediction from the model
        k = 3
        with torch.no_grad():
            output = model(input_tensor)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            topk_probs, topk_classes = torch.topk(probabilities, k)
            #confidence, predicted_idx = torch.max(probabilities, dim=0)

        for i in range(k):
            predicted_class_id = topk_classes[i].item() + 1
            predicted_class = labels.get(predicted_class_id, "Unknown")
            st.markdown(f"<p>{i+1}.<strong style=\"color:green;\">{predicted_class}</strong>(confidence : {topk_probs[i].item()*100:.2f}%)</p> ", unsafe_allow_html=True)

        st.image(image)

        # The picture is saved in the folder named after the species predicted by the model
        upload_folder = os.path.join('static','uploads', predicted_class)
        os.makedirs(upload_folder, exist_ok=True)
    
        contents = os.listdir(upload_folder)
        for item in contents:
            item_path = os.path.join(upload_folder, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
        
        image_path = os.path.join(upload_folder, file.name)
        image.save(image_path)

st.button("Submit", type="primary", on_click=submited)
