import streamlit as st

st.set_page_config(layout='wide')
# Hide the "Switch Page" menu
hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# .st-emotion-cache-6qob1r eczjsme3 {visibility: hidden;}
st.title("Plant Disease Detection and Weather Forecasting App")
if st.button("Login"):
    st.switch_page('pages/login.py')

if st.button("Sign Up"):
    st.switch_page('pages/signup.py')