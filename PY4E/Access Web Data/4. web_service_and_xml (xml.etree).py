# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# You do not need to save these files to your folder since your program will read the data directly from the URL. 

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
xml = urllib.request.urlopen(url).read()

#Read xml string and turn back tree object
tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')

#Look through all the <comment> tags and extract the <count> values
number = []
for item in lst:
    number.append(item.find('count').text)
total = list(map(int, number))

print('Retrieved', len(xml), 'characters')
print('Count:', len(number))
print('Sum:', sum(total))
