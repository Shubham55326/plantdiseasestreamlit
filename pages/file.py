import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import pymongo
from pymongo import MongoClient
import pandas as pd
from PIL import Image

hide_menu_style ="""
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

client = MongoClient('mongodb+srv://shubhammeena55326:7067%40Smeena@cluster0.i87egsm.mongodb.net/?tls=true&tlsAllowInvalidHostnames=true&tlsAllowInvalidCertificates=true')
db = client['lab']
collection1 = db['PlantDisease']
doc = collection1.find({},{"_id":0,'name':1,'children.name':1})
for i in doc:
    classes = i['children']
value = []
for i in range(len(classes)):
    value.append(classes[i]['name'])
data = pd.DataFrame(value)
for i in data:
    cla = data[i]

def predictimage12(uploaded_image):
    loaded_model = load_model('model/PlantDiseaseDetection.h5')
    image = Image.open(uploaded_image)
    image = np.resize(image,(256,256,3))
    image = tf.keras.utils.img_to_array(image)
    image = np.expand_dims(image,axis = 0)
    result = loaded_model.predict(image)
    score = tf.nn.softmax(result[0])
    st.title(cla[np.argmax(score)])
st.title("Predict By Image File ")
file = st.file_uploader('Choose Your File')
if st.button('Predict'):
    predictimage12(file)
if st.button("Home"):
    st.switch_page('pages/plantdisease.py')