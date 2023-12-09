import requests
import csv
from tqdm import tqdm

from multiprocessing import Pool


def get_html(url):
    resp = requests.get(url)
    html = resp.text
    print('loaded page')
    return html


def write_csv(data):
    with open('websites.csv', 'a') as file:
        orders = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(file, fieldnames=orders)
        writer.writerow(data)

def get_page_data(html):
    data = html.strip().split('\n')[1:]
    for row in data:
        columns = row.strip().split('\t')
        name = columns[0]
        url = columns[1]
        description = columns[2]
        traffic = columns[3]
        percent = columns[4]

        data = {'name': name,
                'url': url,
                'description': description,
                'traffic': traffic,
                'percent': percent}
        write_csv(data)


def make_all(url):
    html = get_html(url)
    get_page_data(html)

def main():
    url = 'https://www.liveinternet.ru/rating/ru/today.tsv?page=1'
    response = get_html(url)
    # общее число записей
    count = response.strip().split('\n')[0].split('\t')[1]
    # количество страниц = общее число записей / 30
    pages = round(int(count) / 30)


    url = 'https://www.liveinternet.ru/rating/ru/today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 100)]

    # make_all(url1) -> 1 поток
    # make_all(url2) -> 2 поток
    # make_all(url3) -> 1 поток

    with Pool(10) as p:
        p.map(make_all, urls)





main()