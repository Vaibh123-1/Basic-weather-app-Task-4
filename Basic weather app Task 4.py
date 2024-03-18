import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Unable to display weather data.")

if __name__ == "__main__":
    api_key = "42c652a386f68ce27d6ab5293bfc7bc8"  # Replace with your OpenWeatherMap API key
    location = input("Enter city or zip code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)
