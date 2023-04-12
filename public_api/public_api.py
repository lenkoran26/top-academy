import requests
from random import randint

URL: str = 'https://api.hh.ru/vacancies?'

headers: dict = {
    'User-Agent': 'api-test-agent'
}

params: dict = {
    'page': '1',
    'per_page': '100',
    'text': 'python',
    'area': '2'

}
ids: list = [str]
resp = requests.get(URL, headers = headers, params = params)
data = resp.json()
count_page = data['pages']
count_id = data['found']
#print(resp.status_code)

for i in range(count_page + 1):
    resp = requests.get(f'https://api.hh.ru/vacancies?page={i}&per_page=100&text=python&area=2')
    data = resp.json()
    for item in data['items']:
        ids.append(item['id'])
print(f'found ids = {count_id}, parsed ids = {len(ids)}')
#print(len(set(ids)))

rand_id = ids[randint(0, len(ids)-1)]
url_rand_vacancies = f'https://api.hh.ru/vacancies/{rand_id}'

resp_vacancies = requests.get(url=url_rand_vacancies, headers=headers).json()
print(f'name: {resp_vacancies["name"]}, created_at: {resp_vacancies["created_at"]}, salary: {resp_vacancies["salary"]}, url: {resp_vacancies["alternate_url"]}')
