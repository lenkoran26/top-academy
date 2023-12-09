import requests
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent

URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"

def get_html(url):
    ua = UserAgent().random
    HEADERS = {'User-Agent': ua}

    response = requests.get(url, headers=HEADERS)
    html = response.text

    return html

def get_weather_spb(html):
    soup = Bs(html, 'html.parser')
    date = soup.find('div', class_='dates short-d').text
    table_weather_today = soup.find('table', class_='weather-today short')
    rows_table_today = table_weather_today.find_all(name='tr')
    weather_day_list = []

    for row in rows_table_today:
        # для каждого времени суток создаем свой словарь
        info_weather = {}
        info_weather['weather_day'] = row.find('td', 'weather-day').text
        info_weather['temperature'] = row.find('td', 'weather-temperature').text
        info_weather['tooltip'] = row.find('div')['title']
        info_weather['weather-feeling'] = row.find('td', 'weather-feeling').text
        info_weather['weather-humidity'] = row.find('td', 'weather-humidity').text
        info_weather['weather-probability'] = row.find('td', 'weather-probability').text

        weather_day_list.append(info_weather)
        # в начало списка заносим дату
    weather_day_list.insert(0, date)

    return weather_day_list

html = get_html(URL)

# for item in get_weather_spb(html):
#     print(item)

if __name__ == '__main__':
    print(*get_weather_spb(html), sep='\n')


