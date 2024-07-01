import requests

def get_weather(city):
    api_key = '18d531d3d525ca22d939cf6d'  # Replace with your OpenWeatherMap API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data['cod'] == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize()
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    print("Welcome to the Weather App!")
    city = input("Enter city name: ")
    weather = get_weather(city)

    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("Weather data not available. Please try again.")

if __name__ == "__main__":
    main()
