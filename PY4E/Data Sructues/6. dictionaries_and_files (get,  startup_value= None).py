fname = input("Enter file name: ")
fh = open(fname)

sender_list = list()
for lx in fh:
    lx = lx.rstrip()
    if not lx.startswith("From "):
        continue
    else:
        content = lx.split()
        sender_list.append(content[1])

count = dict()
for name in sender_list:
    #retrieve/create/update counter
    count[name] = count.get(name, 0) + 1

#Set start-up value
big_sender = None
big_time = None

#Loop through key-value pairs in dictionary
for sender, time in count.items():
    if big_time is None or time > big_time:
        big_sender = sender #capture/remember the word that was the largest
        big_time = time
print(big_sender, big_time)
