import configparser
import requests

config = configparser.ConfigParser()
config.read_file(open('keys.cfg'))

API_KEY = "7f007f010a5cb2f7fc221339cfb368e1"
CITY = "Miami"

def get_weather_data(api_key, city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        raise Exception(f"Error retrieving data from API: {response.status_code}")
    
try:
    weather_data = get_weather_data(api_key=API_KEY, city=CITY)
    print("Weather data fetched successfully!")
    print(weather_data)  
except Exception as e:
    print(e)
