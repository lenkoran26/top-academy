from bs4 import BeautifulSoup

def get_course():
    file_html = open('course.html', 'r')

    html = file_html.read()
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('div', 'module-tableSort')
    rows = table.findAll('tr')
    my_dict = {}

    for row in rows:
        if row.find('td', 't-left') and row.find('td', 't-right'):
            k_i = row.find('td', 't-left').text.index('\n')
            k = row.find('td', 't-left').text[:k_i]
            v = row.find('td', 't-right').text.strip('\n')
            my_dict[k.strip('\n')] = v
    return my_dict

if __name__ == '__main__':
    for item in get_course().items():
        print(item)