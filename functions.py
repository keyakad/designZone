import requests
import json

base_url = 'https://api.unsplash.com/'

def imageSearcher(query,num,access_key):
    unsplash_url = base_url + 'search/photos/?client_id=' + access_key + "&" + "query=" + query + "&per_page=" + str(num)
    response = requests.get(unsplash_url)
    udata = json.loads(response.text)
    photos = udata['results']
    x=[]
    for photo in photos:
        x.append(photo['urls']['regular'])
    return x

url = 'http://colormind.io/api/'
def colorPalette(red=0,green=0,blue=0):
    if red < 0:
        red = 0
    elif red > 255:
        blue = 255
    if blue < 0:
        blue = 0
    elif blue > 255:
        blue = 255
    if green < 0:
        green = 0
    elif green > 255:
        green = 255
    data = {
        'model': 'default',
        'input': [[red,green,blue]]
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()['result']
        colors = [('#%02x%02x%02x' % tuple(c)).upper() for c in result]
        return(colors)
    else:
        print('Error:', response.status_code)
