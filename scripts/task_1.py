import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='intro').find('div', class_='wp-block-column is-layout-flow wp-block-column-is-layout-flow').find('h1').text
    # h1 = soup.find('h1', 'wp-block-wporg-random-heading has-heading-cta-font-size').text
    return h1



def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()