import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    fact = data['fact']

    return fact

for i in range(10):
    print(get_cat_fact())