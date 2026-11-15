import requests
from getpass import getpass
url = "https://api.openweathermap.org/data/2.5/weather"
city = input("Введите название города: ")
api_key = getpass("Введите API-ключ OpenWeather: ")
params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "ru"
}
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    print("Город:", city)
    print("Температура:", temperature, "°C")
    print("Погода:", description)

except requests.exceptions.HTTPError as error:
    print("Произошла HTTP-ошибка:", error)
    print("Код ответа сервера:", response.status_code)
    print("Ответ сервера:", response.text)

except requests.exceptions.RequestException as error:
    print("Ошибка соединения:", error)
