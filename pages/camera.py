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


hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

client = MongoClient('mongodb+srv://shubhammeena55326:7067%40Smeena@cluster0.i87egsm.mongodb.net/')
db = client['lab']
collection = db['PlantDisease']
doc = collection.find({},{"_id":0,'name':1,'children.name':1})
for i in doc:
    classes = i['children']
value = []
for i in range(len(classes)):
    value.append(classes[i]['name'])
data = pd.DataFrame(value)
for i in data:
    cla = data[i]

def predictimage(uploaded_image):
    loaded_model = load_model('model/PlantDiseaseDetection.h5')
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
