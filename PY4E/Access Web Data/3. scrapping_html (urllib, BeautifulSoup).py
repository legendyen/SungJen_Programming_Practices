# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
sum = 0
tags = soup('span')
for tag in tags:
    # # Look at the parts of a tag
    # print('TAG:', tag)
    # # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # # print('Attrs:', tag.attrs)
    number = tag.contents[0]
    count = count + 1
    sum = sum + int(number)

print('Count', count)
print('Sum', sum)
