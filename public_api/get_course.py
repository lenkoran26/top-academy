import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
URL = 'https://www.alta.ru/currency/'
response = requests.get(URL, headers={'User-agent': ua.random})

html = response.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('div', class_='module-tableSort')
rows = table.findAll('tr')
my_dict = {}

for row in rows:
    valute = row.find('td', class_='t-left')
    price = row.find('td', class_='t-right')
    my_dict[valute] = price

for i in my_dict.items():
    print(i)