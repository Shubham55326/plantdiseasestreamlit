import streamlit as st
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image


hide_menu_style = """
    <style>
        .st-emotion-cache-6qob1r {visibility: hidden;}
        .st-emotion-cache-zq5wmm {visibility: hidden;}
        .st-emotion-cache-a8g6vw {visibility: hidden;}
        .st-emotion-cache-ch5dnh {visibility: hidden;}
        .st-emotion-cache-rawifx {visibility: hidden}
        .st-emotion-cache-aw8l5d {visibility: hidden;}
        .footer{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: black;
            color: black;
            text-align: center;
        }
        .github{
    
            display: inline-flex;
            vertical-align: top;
            margin: 0 30px;
        }
        .linked{
            display: inline-flex;
            vertical-align: top;
        }
        .facebook{
            display: inline-flex;
            margin: 0 30px;
            vertical-align: top;
        }
        .header{
            text-align: right;
            padding: 10px;
            background-color: rgba(197, 192, 192, 0.534);

        }
        .aboutus , .contactus{
            display: inline-block;
            vertical-align: middle;
            margin: 0 10px;
        }
    </style>
    <header class="header">
        <div class="aboutus"><a href="pages/aboutus.py"><img height="30px" width="30px" src="https://img.icons8.com/?size=100&id=hpQTfjUkuQEs&format=png&color=000000" alt="aboutus"></a></div>
        <div class="contactus"><a href="pages/contactus.py"><img height="30px" width="30px" src="https://img.icons8.com/?size=100&id=43480&format=png&color=000000" alt="contactus"></a></div>
    </header>
    <footer class="footer">
        <h4>Developed By : Shubham Meena</h4>
        <div class="github"><a href="https://github.com/Shubham55326"><img height = "48px" width="50px" src="https://img.icons8.com/?size=100&id=AZOZNnY73haj&format=png&color=000000" alt="github"></a></div>
        <div class="linked"><a href="https://www.linkedin.com/in/shubham-meena-a46695228"><img height="50px" width="50px"  src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="linkedin"></a></div>
        <div class="facebook"><a href="https://www.facebook.com/ShubhamMeena55326?mibextid=ZbWKwL"><img height = "50px" width="50px" src ="https://img.icons8.com/?size=100&id=13912&format=png&color=000000" alt="facebook"></a></div>
    </footer>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

data = [
    "Apple__Apple_scab",
    "Apple__Black_rot",
    "Apple__Cedar_apple_rust",
    "Apple__healthy",
    "Blueberry__healthy",
    "Cherry_(including_sour)__healthy",
    "Cherry_(including_sour)__Powdery_mildew",
    "Corn_(maize)__Cercospora_leaf_spot Gray_leaf...",
    "Corn_(maize)__Common_rust_",
    "Corn_(maize)__healthy",
    "Corn_(maize)__Northern_Leaf_Blight",
    "Grape__Black_rot",
    "Grape__Esca_(Black_Measles)",
    "Grape__healthy",
    "Grape__Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Orange__Haunglongbing_(Citrus_greening)",
    "Peach__Bacterial_spot",
    "Peach__healthy",
    "Pepper,_bell__Bacterial_spot",
    "Pepper,_bell__healthy",
    "Potato__Early_blight",
    "Potato__healthy",
    "Potato__Late_blight",
    "Raspberry__healthy",
    "Soybean__healthy",
    "Squash__Powdery_mildew",
    "Strawberry__healthy",
    "Strawberry__Leaf_scorch",
    "Tomato__Bacterial_spot",
    "Tomato__Early_blight",
    "Tomato__healthy",
    "Tomato__Late_blight",
    "Tomato__Leaf_Mold",
    "Tomato__Septoria_leaf_spot",
    "Tomato__Spider_mites Two-spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_mosaic_virus",
    "Tomato__Tomato_Yellow_Leaf_Curl_Virus"
]

# Convert to DataFrame
data = pd.DataFrame(data, columns=["Plant_Disease"])
for i in data:
    cla = data[i]


def predictimage(uploaded_image):
    loaded_model = tf.keras.models.load_model('model/PlantDiseaseDetection.h5')
    image = Image.open(uploaded_image)
    image = np.resize(image,(256,256,3))
    image = tf.keras.utils.img_to_array(image)
    image = np.expand_dims(image,axis = 0)
    result = loaded_model.predict(image)
    score = tf.nn.softmax(result[0])
    st.title(cla[np.argmax(score)])
st.title("Predict By Capture Image ")
cam = st.camera_input('Capture  Image')
if st.button('Predict'):
    predictimage(cam)

if st.button("Home"):
    st.switch_page('pages/plantdisease.py')
