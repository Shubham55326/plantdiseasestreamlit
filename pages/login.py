import streamlit as st
from pymongo import MongoClient
import ssl
hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

client = MongoClient('mongodb+srv://shubhammeena55326:7067%40Smeena@cluster0.i87egsm.mongodb.net/test?retryWrites=true&w=majority',ssl=True,
    ssl_cert_reqs=ssl.CERT_NONE)

db = client['lab']

def login(username2,password2):
    collection2 = db['UserData']
    user2 = collection2.find_one({'Username':username2})
    if user2 and user2['Password'] == password2:
        st.switch_page("pages/plantdisease.py")
    st.write('Invalid Username Or Password')



user2 = st.text_input('Username')
pass2 = st.text_input('Password',type='password')
if st.button('Login'):
    res2 = login(user2,pass2)
if st.button('Click Here to Create Account'):
    st.switch_page('pages/signup.py')
    