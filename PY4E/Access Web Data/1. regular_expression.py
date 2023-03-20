# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
handle = open('regex_sum_1764860.txt')

total = list()
for line in handle:
    line = line.rstrip()
    item = re.findall('[0-9]+', line)
    if len(item) == 0:
        continue
    total = total + item
print(total)

sum = 0
for i in total:
    i = int(i)
    sum = sum + i
print(sum)
