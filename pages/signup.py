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
