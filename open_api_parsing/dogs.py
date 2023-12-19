import requests

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

data = response.json()
image_url = data['message']
image = requests.get(image_url).content
with open('image.jpg', 'wb') as file:
    file.write(image)