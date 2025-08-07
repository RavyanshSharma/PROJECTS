
import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:
    city = input("Enter the city (or 'exit' to quit): ")
    if city.lower() == "exit":
        break
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=[ENTER YOUR API KEY HERE]={city}"
        r = requests.get(url)
        data = json.loads(r.text)

        temp = data["current"]["temp_c"]
        wind = data["current"]["wind_kph"]
        winddir = data["current"]["wind_dir"]
        humidity = data["current"]["humidity"]

        message = f"The weather in {city} is {temp} degrees Celsius, wind speed is {wind} kilometers per hour, wind direction is {winddir}, and humidity is {humidity} percent."
        print(message)
        speak(message)

    except Exception as e:
        print("Something went wrong:", e)

        speak("Sorry, I could not get the weather information.")
