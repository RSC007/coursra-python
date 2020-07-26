# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

########################################################################################################
## 
'''
1 > Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
2 > Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kaelum.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: E '''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ul = list()


def fetch_url(urls):
    link = list()
    for url in urls:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            break
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    i=1
    for tag in tags:
        if int(position)==i:
            link.append(tag.get('href', None))
            break
        i +=1
    return link

ul.append(input('Enter - '))
count = input('Enter counts: ')
position = input('Enter the position: ')
print('Retreving: ',ul)
a= 0
while (a<int(count)):
    p = ul[a]
    temp = list()
    temp.append(p)
    fetch = fetch_url(temp)
    print('Retreving: ',fetch)
    if not fetch in ul: # only new email add into our parent list
        ul = ul + fetch # Concatinate the list to ignore '['l1',['l2']]' and get the output ['l1','l2']
    a +=1

