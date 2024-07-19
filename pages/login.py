import streamlit as st
from pymongo import MongoClient
hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
        .st-emotion-cache-zq5wmm {visibility: hidden;}
        .st-emotion-cache-a8g6vw {visibility: hidden;}
        .st-emotion-cache-ch5dnh {visibility: hidden;}
        .st-emotion-cache-rawifx {visibility: hidden}
        .st-emotion-cache-aw8l5d {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

client = MongoClient('mongodb+srv://shubhammeena55326:7067%40Smeena@cluster0.i87egsm.mongodb.net/?tls=true&tlsAllowInvalidHostnames=true&tlsAllowInvalidCertificates=true')
db = client['lab']

def login(username2,password2):
    collection2 = db['UserData']
    user = collection2.find_one({'Username':username2})
    if user and user['Password'] == password2:
        st.switch_page("pages/plantdisease.py")
    st.write('Invalid Username Or Password')



st.title("Log In")
user2 = st.text_input('Username')
pass2 = st.text_input('Password',type='password')
if st.button('Login'):
    res2 = login(user2,pass2)
if st.button('Click Here to Create Account'):
    st.switch_page('pages/signup.py')
