import streamlit as st


hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.write("Predict By Image File")
if st.button("Predict By File"):
    st.switch_page('pages/file.py')
st.write("Predict By Capture Image ")
if st.button("Predict By Image Captured By Camera"):
    st.switch_page('pages/camera.py')
st.write("Weather ForeCasting")
if st.button("Click Here For Weather Forecasting"):
    st.switch_page('pages/weather.py')
st.write('Log Out')
if st.button('Log Out'):
    st.switch_page('home.py')