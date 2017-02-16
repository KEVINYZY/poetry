#coding=utf-8
#import poetspider

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

for i in result:
    poem = i.encode('utf-8')
    fh2.write(poem)          

poems=[]
for i in result:
    poem = i.encode('utf-8')
    poems.append(poem)


countingdict={}
print 'finishanalysis'

for i in poems:
    if i in countingdict:
        countingdict[i]= countingdict[i]+1
    else:
        countingdict[i] = 1

summary = 0
for i in countingdict:
    summary = countingdict[i]+summary



for i in countingdict:
    fh3.write(i+':'+str(countingdict[i])+str(countingdict[i]/summary)+'\n')

print summary

fh.close()
fh2.close()
fh3.close()






