import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c0e0d91a427a1c17afefaa07272ef401"
account_sid = 'AC9aa08f8413553b8893bb474f7b8cf790'
auth_token = "040352f21201d88e96e9587c38e4659f"

weather_params = {
  "lat": 19.075983,
  "lon": 72.877655,
  "appid": api_key,
  "cnt": 4
  
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0])

for hour_data in weather_data["list"]:
   condition_code = hour_data["weather"][0]["id"]
   if int(condition_code) < 700:
       will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "It will rain today",
        from_='+16693228832',
        to='+919833816151'
    )
    print(message.status)