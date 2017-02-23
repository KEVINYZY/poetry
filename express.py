#coding=utf-8
import sqlite3
import jieba
poem_count = {}

poem_base = sqlite3.connect('poems.db')

try:
    poem_base.execute('''CREATE TABLE EXPRESS(id INT PRIMARY KEY   NOT NULL,express   TEXT NOT NULL,count   INT NOT NULL);''')
except:
    print 'table "EXPRESS" is already exist'


poem_tablet = poem_base.execute("select * from POEMS")
poems = poem_tablet.fetchall()

poem_list = []

for poem in poems:
    sentence = poem[1]
    result = jieba.lcut(sentence,cut_all=True)
    poem_list.extend(result)

print '分词完毕，正在写入数据库...'



for i in poem_list:
    if i in poem_count:
        poem_count[i] = poem_count[i]+1
    else:
        poem_count[i] = 1



ident = 0
for key in poem_count:
    values = (ident,key,poem_count[key])
    poem_base.execute("insert into EXPRESS values(?,?,?)",values)
    ident = ident+1


poem_base.execute("delete from EXPRESS where id = 0")  

poem_base.commit()
poem_base.close()

print '写入完毕，退出'
















