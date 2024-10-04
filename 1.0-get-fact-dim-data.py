import configparser
import datetime
import requests


config = configparser.ConfigParser()
config.read_file(open('keys.cfg'))

API_KEY = config.get("openweathermap", "API_KEY")
CITY = "Miami"


def get_weather_data(api_key, city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        raise Exception(f"Error retrieving data from API: {response.status_code}")
    

def get_fact_dim_data(data):
    weather_fact = {
        'temperature': data['main']['temp'],
        
    }