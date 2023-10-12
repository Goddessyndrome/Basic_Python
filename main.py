import requests
import json
import pyttsx3  # Import pyttsx3
import os

city = input("Enter the name of the city:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r = requests.get(url)
print(r.text)
weather_data = json.loads(r.text)
temperature_celsius = weather_data["current"]["temp_c"]


engine = pyttsx3.init()
text_to_speak = f'The current weather in {city} is {temperature_celsius} degrees Celsius.'
engine.say(text_to_speak)
engine.runAndWait()
