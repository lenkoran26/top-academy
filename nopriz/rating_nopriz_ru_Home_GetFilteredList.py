import requests

from requests import Request, Session


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'multipart/form-data',
    'Origin': 'http://rating.nopriz.ru',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0, no-cache',
    'Pragma': 'no-cache',
}

files = {
    'maxSum': (None, 0),
    'IsGosContract':(None, False),
    'FilterText':(None, ''),
    'ActivityDirectionId':(None, 1)
}

response = requests.post('http://rating.nopriz.ru/Home/GetFilteredList', files=files)
data = response.json()['list']['items'][0]
print(response.content)