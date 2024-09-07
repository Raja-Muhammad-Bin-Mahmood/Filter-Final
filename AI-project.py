import requests
import streamlit as st
import random
import time

# Set up the page
st.set_page_config(layout="wide")

# Styling with the design and color scheme inspired by the image
st.markdown("""
    <style>
    body {background-color: #131f2e;}
    .stText {color: #d1e8ff; font-family: 'Poppins', sans-serif;}
    .stBox {background-color: #1f354f; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stGreenBox {background-color: #238636; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stTitle {font-size: 2.5em; font-weight: bold; text-align: center; color: #d1e8ff; font-family: 'Poppins', sans-serif;}
    .stBorder {border: 3px solid #0a74da; border-radius: 20px; padding: 10px; margin-bottom: 20px;}
    .bold-text {font-weight: bold; font-size: 1.2em;}
    </style>
""", unsafe_allow_html=True)

# Title with custom font
st.markdown('<h1 class="stTitle">Water Filtration Plants PD Khan Thill Sharif</h1>', unsafe_allow_html=True)

# Weather API setup (OpenWeatherMap)
api_key = "your_openweather_api_key_here"  # Replace this with your OpenWeather API key
latitude = 32.6970
longitude = 73.3252

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Dynamic data section (inside st.empty())
placeholder = st.empty()

# Function to display the data fetched
def display_data():
    # Fetch the weather data from the API
    weather_data = fetch_weather_data()
    
    if weather_data and "main" in weather_data:
        temp_c = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_desc = weather_data['weather'][0]['description'].capitalize()
    else:
        temp_c = random.uniform(22.0, 25.0)
        humidity = random.randint(60, 80)
        weather_desc = "No data"

    with placeholder.container():
        # Create three columns for three different filtration systems
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="stBox stBorder"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(400, 500)} Liters/day</p>', unsafe_allow_html=True)
            st.markdown(f'<h4>REAL TIME DATA</h4>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Mineral Dosage: {random.randint(5, 15)} kg/day</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Filter Life: {random.randint(70, 90)}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Estimated Beneficiary Today: {random.randint(1000, 5000)} people (Increase: {random.randint(1, 5)}%)</p>', unsafe_allow_html=True)
            st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="stBox stBorder"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(350, 450)} Liters/day</p>', unsafe_allow_html=True)
            st.markdown(f'<h4>REAL TIME DATA</h4>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Mineral Dosage: {random.randint(7, 12)} kg/day</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Filter Life: {random.randint(75, 95)}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Estimated Beneficiary Today: {random.randint(1200, 5200)} people (Increase: {random.randint(2, 6)}%)</p>', unsafe_allow_html=True)
            st.markdown('<div class="stGreenBox">Maintenance done 25 days ago. Next maintenance due in 35 days.</div></div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="stBox stBorder"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(380, 480)} Liters/day</p>', unsafe_allow_html=True)
            st.markdown(f'<h4>REAL TIME DATA</h4>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Mineral Dosage: {random.randint(6, 14)} kg/day</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Filter Life: {random.randint(60, 85)}%</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="bold-text">Estimated Beneficiary Today: {random.randint(1100, 5100)} people (Increase: {random.randint(3, 7)}%)</p>', unsafe_allow_html=True)
            st.markdown('<div class="stGreenBox">Maintenance done 20 days ago. Next maintenance due in 30 days.</div></div>', unsafe_allow_html=True)

# Main loop to update data every 5 seconds
while True:
    display_data()
    time.sleep(2)  # Sleep for 2 seconds between updates
