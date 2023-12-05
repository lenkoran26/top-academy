import requests
from bs4 import BeautifulSoup as bs


URL_1 = "https://reestr.nopriz.ru/api/sro/list"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br"
    }
DATA = {
    "filters":{},
    "page":1,
    "pageCount":"20",
    "sortBy":{}}


response = requests.post(url=URL_1, headers=HEADERS, data=DATA)
data = response.json()['data']['data'][0]
pass