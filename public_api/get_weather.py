import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
response = requests.get(URL, headers={'User-agent': ua.random})

html = response.text
soup = BeautifulSoup(html, 'html.parser')

date = soup.find('div', class_='dates short-d').text
table = soup.find('table', class_='weather-today short')

#table.find('tr', class_='night')
#table.find('tr', class_='night').find('td', class_='weather-temperature')
#table.find('tr', class_='night').find('td', class_='weather-temperature').find('span').text

t_night = table.find('tr', class_='night').find('td', class_='weather-temperature').find('span').text
t_morning = table.find('tr', class_='morning').find('td', class_='weather-temperature').find('span').text
t_day = table.find('tr', class_='day').find('td', class_='weather-temperature').find('span').text
t_evening = table.find('tr', class_='evening').find('td', class_='weather-temperature').find('span').text

weather_today: dict[str,str] = {}
weather_today['night'] = t_night
weather_today['morning'] = t_morning
weather_today['day'] = t_day
weather_today['evening'] = t_evening

print(date)
print(weather_today)
pass