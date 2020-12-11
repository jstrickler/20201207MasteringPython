import requests   # not in std library

URL = "https://www.home-assistant.io/"


try:
    response = requests.get(URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:
        content = response.content.decode()
        print(content)

IMAGE_URL = "https://www.home-assistant.io/images/blog/2020-09-15-home-assistant-tags/tag-reader.jpg"

try:
    response = requests.get(IMAGE_URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:
        with open('tag-reader.jpg', 'wb') as jpg_out:
            jpg_out.write(response.content)
