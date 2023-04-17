import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_weather_spb() -> list:
    ua = UserAgent()
    URL: str = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
    response = requests.get(URL, headers={'User-agent': ua.random})

    html: str = response.text
    soup = BeautifulSoup(html, 'html.parser')

    date: str = soup.find('div', class_='dates short-d').text
    table_weather_today = soup.find('table', class_='weather-today short')

    rows_table_today = table_weather_today.find_all(name='tr')
    weather_day_list: list = [dict]

    for row in rows_table_today:
        info_weather: dict = {str: str}
        info_weather['weather_day'] = row.find('td', class_='weather-day').text
        info_weather['temperature'] = row.find('td', class_='weather-temperature').text
        info_weather['tooltip'] = row.find('div')['title']
        info_weather['weather-feeling'] = row.find('td', class_='weather-feeling').text
        info_weather['weather-humidity'] = row.find('td', class_='weather-humidity').text
        weather_day_list.append(info_weather.copy())

    weather_day_list.insert(0, date)

    return weather_day_list


# t_night = table_weather_today.find('tr', class_='night').find('td', class_='weather-temperature').find('span').text
# t_morning = table_weather_today.find('tr', class_='morning').find('td', class_='weather-temperature').find('span').text
# t_day = table_weather_today.find('tr', class_='day').find('td', class_='weather-temperature').find('span').text
# t_evening = table_weather_today.find('tr', class_='evening').find('td', class_='weather-temperature').find('span').text

