import streamlit as st


hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if st.button("Predict By File"):
    st.switch_page('pages/file.py')

if st.button("Predict By Image Captured By Camera"):
    st.switch_page('pages/camera.py')

if st.button("Click Here For Weather Forecasting"):
    st.switch_page('pages/weather.py')
