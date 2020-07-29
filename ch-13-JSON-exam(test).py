import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


serviceurl = 'http://py4e-data.dr-chuck.net/comments_704588.json?' # chnage this link to which url data you want fetch

# Ignore SSL certificate errors


while True:
    address = input('Enter location: ')
    if len(address)<1: break             # to exit the infinity loop press 'enter'

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read().decode()              # your whole data convert from utf-8 stnderd to human readble formate as it is 
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None

    total = 0
    for count in js["comments"]:
        x = count["count"]
        total = total + int(x)
    print(total)
    