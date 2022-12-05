import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    r = requests .get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
    data = r.json()
    city = data['name']
    cur_temp = data['main']['temp']
    cur_hum = data['main']['humidity']
    cur_press = round((data['main']['pressure'] * 10**2) /133)
    cur_wind = data['wind']['speed']

    print(f"Погода в городе {city} в данный момент:\n"
          f"Температура: {cur_temp} градусов по Цельсию\n"
          f"Влажность: {cur_hum}%\n"
          f"Давление: {cur_press} мм рт ст\n"
          f"Скорость ветра: {cur_wind} м/c")
def city_weather():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

city_weather()
print('')
def covid():
    state = input("Ведите код штата про ковид-обстановку которого вы хотели бы узнать ")
    date = int(input("Ведите дату в формате ггггммдд "))
    day=str(date)[-2:]+"."+str(date)[-4:-2]+"."+str(date)[:-4]
    r = requests.get(f'https://api.covidtracking.com/v1/states/{state}/{date}.json')
    data = r.json()
    num_death=data['death']
    num_death_today=data['deathIncrease']
    num_hospitalized=data['hospitalizedCurrently']
    num_hospitalized_today=data['hospitalized']
    num_recovered=data['recovered']
    print(f"Информация про количество заболевших в штате с кодом {state} за {day}:\n"
    f"За этот день от ковида погибло {num_death_today} людей, за всю пандемию в этом штате погибло {num_death} людей\n"
    f"В этот день было госпитализированно {num_hospitalized_today} людей, всего на данный момент госпитализированно {num_hospitalized} людей\n"
    f"За эти сутки выздоровело {num_recovered} людей")

covid()