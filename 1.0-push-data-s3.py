import configparser
import requests
import json
from datetime import datetime
import boto3



config = configparser.ConfigParser()
config.read_file(open('keys.cfg'))

API_KEY = config.get("openweathermap", "API_KEY")
CITY = "Miami"


def get_weather_data(api_key, city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  
    else:
        raise Exception(f"Error retrieving data from API: {response.status_code}")
    

def upload_to_s3(bucket_name, data, key):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))


if __name__ == '__main__':

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    weather_data = get_weather_data(api_key=API_KEY, city=CITY)

    weather = {
        'date_id': timestamp,
        'temperature': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
        'humidity': weather_data['main']['humidity'],
        'wind_speed': weather_data['wind']['speed'],
        'cloudiness': weather_data['clouds']['all'],
        'insert_timestamp': timestamp
    }

    upload_to_s3(bucket_name='weather-bucket-jpb', 
                 data=weather,
                 key=f'data/{timestamp}.json'
            )