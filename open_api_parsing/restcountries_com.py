import requests

url_all = "https://restcountries.com/v3.1/all"
url_country = "https://restcountries.com/v3.1/name/deutschland"
url_capital = "https://restcountries.com/v3.1/capital/moscow"

response = requests.get(url_capital)

data = response.json()
print(data)