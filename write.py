#coding=utf-8
import sqlite3
import random
import pypinyin
from pypinyin import pinyin, lazy_pinyin

'''
先试试七言绝句
'''
poem_base = sqlite3.connect('poems.db')
express_tablet = poem_base.execute("select * from EXPRESS")

numbers = 0
resause = []

sentence=''

lenth = 0

for i in express_tablet:
    resause.append(i[1])

resause = list(set(resause))

'''
ryme = {}
ryme_list = []
final_ryme_list = []

for i in resause:
    result = pypinyin.pinyin(i,style=5)
    ryme[i] = result
    ryme_list.extend(result)




for i in ryme_list:
    final_ryme_list.extend(i)

ryme_list = list(set(final_ryme_list))
#print ryme_list
'''

judge = 1
express = []

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]


express = []

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]

express = []

for i in resause:
    if len(i) == 3:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select] 

yayun = express[select]
yayun = pypinyin.pinyin(yayun,style=5)
yayun = yayun[-1]
#print yayun[0]


for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]


express = []

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]

express = []

for i in resause:
    if len(i) == 3:
        express.append(i)
        
while 1:

    select = random.randint(0,len(express)-1)
    yun = express[select]
    yun = pypinyin.pinyin(yun,style=5)
    yun = yun[-1]
    if yun[0] == yayun[0]:
        sentence = sentence + express[select]
        break
    else:
        continue

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]


express = []

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]

express = []

for i in resause:
    if len(i) == 3:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select] 

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]


express = []

for i in resause:
    if len(i) == 2:
        express.append(i)

select = random.randint(0,len(express)-1)
sentence = sentence + express[select]

express = []

for i in resause:
    if len(i) == 3:
        express.append(i)
        
while 1:

    select = random.randint(0,len(express)-1)
    yun = express[select]
    yun = pypinyin.pinyin(yun,style=5)
    yun = yun[-1]
    if yun[0] == yayun[0]:
        sentence = sentence + express[select]
        break
    else:
        continue

    
result = []
for i in range(0,len(sentence),7):
    seq = sentence[i:i+7]
    express = ''.join(seq)
    result.append(express)













