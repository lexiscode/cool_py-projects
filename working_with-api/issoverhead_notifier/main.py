import requests
from datetime import datetime
import time


MY_LAT = 7.646440  # Your latitude
MY_LONG = 3.922210  # Your longitude

# ISS Current Location documentation link http://open-notify.org/Open-Notify-API/ISS-Location-Now/

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # typecast from str to float
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# Sunrise and Sunset documentation link https://sunrise-sunset.org/api
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data), check out the full dictionary lists
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # split() splits strings and converts them to a list
    # then typecast it from str to int
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_now_hour = time_now.hour

    if time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour:
        return True


while True:
    time.sleep(60) # pauses the loop every 60 secs
    if is_iss_overhead() and is_night():
        print("Look up NOWWW!")

