import streamlit as st

st.set_page_config(layout='wide')
# Hide the "Switch Page" menu
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


st.markdown('''[Contact us](pages/contact.py)''',unsafe_allow_html=True)
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title("Plant Disease Detection and Weather Forecasting App")
if st.button("Login"):
    st.switch_page('pages/login.py')
if st.button("Sign Up"):
    st.switch_page('pages/signup.py')
# .st-emotion-cache-6qob1r eczjsme3 {visibility: hidden;}
    
