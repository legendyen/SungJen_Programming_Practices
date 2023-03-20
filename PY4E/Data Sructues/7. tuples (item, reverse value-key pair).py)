# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file: ")
fh = open(fname)

count = dict()
#Loop through line as string
for lx in fh:
    lx = lx.rstrip()
    if not lx.startswith("From "):
        continue
    #First split string into list of information
    lx = lx.split()
    #Double split time inforamtion to extract hours
    time = lx[5].split(":")
    #Count the time
    count[time[0]] = count.get(time[0], 0) + 1

lst = list()
#Create revesre tuple to store in value-key pairs
for k, v in count.items():
    lst.append((v, k))
    lst = sorted(lst, reverse=True)

#Print out top 5 hours that users send emails
for v, k in lst[:5]:
    print(k, v)
