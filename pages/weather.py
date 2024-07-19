import streamlit as st
import requests
from geopy.geocoders import Photon
# from geopy.geocoders import Nominatim
hide_menu_style = """
    <style>
    .st-emotion-cache-6qob1r {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def weatherforecast(city):
    geolocator = Photon(user_agent="MyApp")
    # geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    url2 = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    url1 = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring1 = {"q":f"{lat},{lon}"}
    querystring2 = {"q":f"{city}","days":"3","lang":"English"}
    headers = {"X-RapidAPI-Key": "ed57433e70mshae16ab55c59e0fap14713bjsnb4b92b668e03","X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}
    response1 = requests.get(url1, headers=headers, params=querystring1)
    response2 = requests.get(url2, headers=headers, params=querystring2)
    res1 = response1.json()
    res2 = response2.json()
    City = res1['location']['name']
    State = res1['location']['region'] 
    Country = res1['location']['country']
    Date_and_Time = res1['location']['localtime']
    Updated = res1['current']['last_updated']
    data_forcast = res2['forecast']['forecastday']
    data_2nd_day = dict(data_forcast[1])
    data_3rd_day = dict(data_forcast[2])
    Temperature1 = res1['current']['temp_c']
    Wind_speed1 = res1['current']['wind_kph']
    Precipitation1 = res1['current']['precip_mm']
    Humidity1 = res1['current']['humidity']
    Cloud1 = res1['current']['condition']['text']
    img1 = res1['current']['condition']['icon']
    date2 = data_2nd_day['date']
    Max_Temperature2 = data_2nd_day['day']['maxtemp_c']
    Min_Temperature2 = data_2nd_day['day']['mintemp_c']
    Wind_speed2 = data_2nd_day['day']['maxwind_mph']
    Precipitation2 = data_2nd_day['day']['totalprecip_mm']
    Humidity2 =data_2nd_day['day']['avghumidity']
    Cloud2 = data_2nd_day['day']['condition']['text']
    img2 = data_2nd_day['day']['condition']['icon']
    Sunrise2 = data_2nd_day['astro']['sunrise']
    Sunset2 = data_2nd_day['astro']['sunset']
    date3 = data_3rd_day['date']
    Max_Temperature3 = data_3rd_day['day']['maxtemp_c']
    Min_Temperature3 = data_3rd_day['day']['mintemp_c']
    Wind_speed3 = data_3rd_day['day']['maxwind_mph']
    Precipitation3 = data_3rd_day['day']['totalprecip_mm']
    Humidity3 =data_3rd_day['day']['avghumidity']
    Cloud3 = data_3rd_day['day']['condition']['text']
    img3 = data_3rd_day['day']['condition']['icon']
    Sunrise3 = data_3rd_day['astro']['sunrise']
    Sunset3 = data_3rd_day['astro']['sunset']
    if not img1.startswith(('http://', 'https://')):
        image_url1 = 'http:' + img1
    if not img2.startswith(('http://', 'https://')):
        image_url2 = 'http:' + img2
    if not img3.startswith(('http://', 'https://')):
        image_url3 = 'http:' + img3
    response = requests.get(image_url1)
    response = requests.get(image_url2)
    response = requests.get(image_url3)
    day1 = st.container(height=500,border=True)
    day1.image(image_url1)
    day1.write(f'Temperature: {Temperature1}')
    day1.write(f'Wind speed: {Wind_speed1}')
    day1.write(f'Precipitation: {Precipitation1}')
    day1.write(f'Humidity: {Humidity1}')
    day1.write(f'Cloud: {Cloud1}')
    day1.write(f'City: {City}')
    day1.write(f'State: {State}')
    day1.write(f'Country: {Country}')
    day1.write(f'Date and Time: {Date_and_Time}')
    day2 = st.container(height=560,border=True)
    day2.image(image_url2)
    day2.write(f'Date: {date2}')
    day2.write(f'Temperature - Max: {Max_Temperature2}')
    day2.write(f'Temperature - Min: {Min_Temperature2}')
    day2.write(f'Wind speed: {Wind_speed2}')
    day2.write(f'Precipitation: {Precipitation2}')
    day2.write(f'Humidity: {Humidity2}')
    day2.write(f'Cloud: {Cloud2}')
    day2.write(f'City: {City}')
    day2.write(f'State: {State}')
    day2.write(f'Country: {Country}')
    day3 = st.container(height=560,border=True)
    day3.image(image_url3)
    day3.write(f'Date: {date3}')
    day3.write(f'Temperature - Max: {Max_Temperature3}')
    day3.write(f'Temperature - Min: {Min_Temperature3}')
    day3.write(f'Wind speed: {Wind_speed3}')
    day3.write(f'Precipitation: {Precipitation3}')
    day3.write(f'Humidity: {Humidity3}')
    day3.write(f'Cloud: {Cloud3}')
    day3.write(f'City: {City}')
    day3.write(f'State: {State}')
    day3.write(f'Country: {Country}')
st.title("Weather ForeCasting")
city = st.text_input("City")
if st.button('Get Data'):
    weatherforecast(city)
if st.button("Home"):
    st.switch_page('pages/plantdisease.py')

    