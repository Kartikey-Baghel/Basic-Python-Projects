import requests

def get_weather(city):
    api_key = "api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        print(response.status_code)
        data = response.json()
        print(data)
        if data.get("cod") != 200:
            print("City not found.")
            return
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    except Exception as e:
        print("Error fetching data:", e)

city_name = input("Enter city name: ")
get_weather(city_name)
