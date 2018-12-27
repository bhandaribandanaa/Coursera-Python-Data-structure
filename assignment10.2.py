#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dct=dict()
for line in handle:
    if line.startswith("From"):
        word=line.split()
        # print(word)
        if(len(word)>2):
            nwords=word[5]
            nword=nwords.split(':')
            nwd=nword[0]
            # print(nwd)s
            dct[nwd]=dct.get(nwd,0) + 1
# print(dct)
lst=list()
for val,key in dct.items():
    newlst=(val,key)
    lst.append(newlst)
lst.sort()
for val,key in lst:
    print(val,key)
# lst= sorted(lst,reverse=True)
