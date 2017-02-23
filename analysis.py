#coding=utf-8
#import poetspider
from collections import defaultdict

import sqlite3

database = sqlite3.connect("poems.db")
try:
    database.execute('''CREATE TABLE POEMS(  id INT    PRIMARY KEY   NOT NULL,poems   TEXT NOT NULL);''')
except:
    print 'table "POEMS" is already exist'

try:
    database.execute('''CREATE TABLE CHARS(  id INT    PRIMARY KEY   NOT NULL,poems   TEXT NOT NULL);''')
except:
    print 'table "CHARS" is already exist'

countingresult = defaultdict(list)
countingdict = {}

fh = open('poems.txt','r')

fh2 = open('poems2.txt','w')
fh2.write('')
fh2.close()
fh2 = open('poems2.txt','a')

fh3 = open('counting.txt','w')
fh3.write('')
fh3.close()
fh3 = open('counting.txt','a')

chars = fh.read()

def is_chinese(uchar): #判断汉字
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    elif uchar in [u'\uff0c', u'\u3002', u'\uff1f', u'\uff01', u'\uff1b',u'\n']:
        return True
    else :
        return False

#allchars = chars.split()
chars = unicode(chars,'utf-8')
a = unicode('（一作','utf-8')
b = unicode('（','utf-8')
chars = chars.replace(a,b)



result = []
for i in chars:
    if is_chinese(i) is True:
        result.append(i)

#print result

n=0
for i in result:
    poem = i.encode('utf-8')
    n=n+1
    fh2.write(poem)
#print n


fh2=open('poems2.txt','r')

n = 0
while True:
    poems = fh2.readline()
    if not poems:
        break
    else:
        if poems == '\n':
            continue
        else:
            n = n+1
            values = (n,unicode(poems,'utf-8'))
            database.execute("insert into POEMS values(?,?)",values)
        
database.commit()
print n

fh2=open('poems2.txt','r')

allpoems = fh2.read()
allpoems = allpoems.replace('\n','')
allpoems = unicode(allpoems,'utf-8')
n = 0

for i in allpoems:
    #print i
    if i is '\n':
        continue
    n = n+1
    values = (n,i)
    database.execute("insert into CHARS values(?,?)",values)
    

database.commit()

print n

poems=[]
for i in result:
    poem = i.encode('utf-8')
    poems.append(poem)

#countingdict={}
#print 'finishanalysis'

for i in poems:
    if i in countingdict:
        countingdict[i] = countingdict[i]+1
    else:
        countingdict[i] = 1

summary = 0
for i in countingdict:
    summary = countingdict[i]+summary

for i in countingdict:
    #countingdict[i].append(countingdict[i]/summary)
    share = float(countingdict[i])/float(summary)
    countingresult[i].append([share])
    fh3.write(i+':'+str(countingdict[i])+str(share)+'\n')

#print countingresult
#print summary
print 'finishanalysis'

fh.close()
fh2.close()
fh3.close()
database.close()

