# weather_tool.py

def weather(city):

    weather_data = {
        "hyderabad": "34°C Sunny",
        "delhi": "38°C Hot",
        "mumbai": "29°C Cloudy",
        "chennai": "33°C Humid",
        "bangalore": "28°C Pleasant"
    }

    return weather_data.get(
        city.lower(),
        "Weather data not available."
    )