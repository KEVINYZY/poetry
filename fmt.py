#coding=utf-8
import write
import sqlite3
import random
import pypinyin

poem = write.sentence

poem_base = sqlite3.connect('poems.db')
char_tablet = poem_base.execute("select * from CHARS")

chars=[]
for i in char_tablet:
    chars.append(i[1])

chars = list(set(chars))

#print chars

from collections import defaultdict
yindiao = defaultdict(list)
rym = defaultdict(list)
yindiaolist=[]

tmp = []
cache = []
for i in chars:
    sound = pypinyin.pinyin(i, style=7)
    tmp.extend(sound)

for i in tmp:
    sound = str(i)
    sound = filter(str.isdigit, sound)
    yindiaolist.append(sound)

for i in yindiaolist:
    array = yindiaolist.index(i)
    yindiao[i].append(chars[array])

#print yindiao
tmp = []
for i in chars:
    ryme = pypinyin.pinyin(i,style=5)
    tmp.extend(ryme)

yunlist = []
for i in tmp:
    yunlist.extend(i)

#print yunlist
for i in yunlist:
    array = yunlist.index(i)
    rym[i].append(chars[array])

#while True:

tmp = []
cache = []
for i in poem:
    if i in tmp:
        ryme = pypinyin.pinyin(i,style=5)
        for j in ryme:
            cache.extend(j)
            z = cache[0]        
        count = len(rym[z])
        get = random.randint(0,count-1)
        changechar = rym[z][get]
        tmp.extend(changechar)
    else:    
        tmp.append(i)

result = []
for i in range(0,len(tmp),7):
    seq = tmp[i:i+7]
    express = ''.join(seq)
    result.append(express)

for i in result:
    print i
