import streamlit as st
from pymongo import MongoClient

hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
client = MongoClient('mongodb+srv://shubhammeena55326:7067%40Smeena@cluster0.i87egsm.mongodb.net/?tls=true&tlsAllowInvalidHostnames=true&tlsAllowInvalidCertificates=true')
db = client['lab']


def signup(name1,username1,password1):
    collection1 = db['UserData']
    if collection1.find_one({'Username':username1}):
        st.write('User Already Exist')
    collection1.insert_one({'Name':name1,'Username':username1,'Password':password1})
    st.switch_page('pages/plantdisease.py')
st.title("Sign Up")
name1 = st.text_input('Name')
user1 = st.text_input('Username')
pass1 = st.text_input('Password',type='password')
if st.button('Signup'):
    res1 = signup(name1,user1,pass1)
if st.button('Already Having Account Click Here'):
    st.switch_page('pages/login.py')
