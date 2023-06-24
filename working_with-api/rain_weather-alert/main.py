import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "c210bdd4c6e230d26642674571bbda19"

weather_params = {
    "lat": 7.646440,
    "lon": 3.922210,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]  # to get the first 12 hours (0-11hours)

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
# this was done below in order not to repeatedly print the same thing for each hour
if will_rain:
    print("It's going to rain today. Remember to bring an ☔")