import urllib.request
import json

url = input('Enter URL: ')
url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()

print('Retrieving ', url)
print('Retrieved', len(data), 'characters')

js = json.loads(data)
info = js['comments']
# print(info)

number = []
for item in info:
    number.append(item['count'])
# print(number)

print('Count:', len(number))
print('Sum:', sum(number))
