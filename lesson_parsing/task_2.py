import requests

def get_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    image_url = data['message']
    image = requests.get(image_url).content

    return image

for i in range(1, 11):
    with open(f'image_{i}.jpg', 'wb') as file:
        file.write(get_dog_image())