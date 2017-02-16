#coding=utf-8
import urllib2
import bs4
from bs4 import BeautifulSoup
import time

starttime = time.clock() 

site = "http://sou-yun.com/PoemIndex.aspx?dynasty=Tang"
requests = urllib2.Request(site)
requests.add_header('User-Agent',"HeJingjing's Browser") 
response = urllib2.urlopen(requests)
site_page = response.read().decode('utf-8')
soup = BeautifulSoup(site_page, 'html.parser')

poemlist = []

tags = soup('a')
for tag in tags:
    address = tag.get('href', None)
    if '/PoemIndex.aspx?dynasty=Tang&author' in address:
        poemlist.append(address) #获取所有诗人的网址列表

poemlists = list(set(poemlist))

#print poemlist 
#上一行仅供测试用，正式代码中请注释掉

def view_poet(url):
    url = 'http://sou-yun.com'+ url
    req = urllib2.Request(url)
    req.add_header('User-Agent',"HeJingjing's Browser") 
    response = urllib2.urlopen(req)
    response.encoding='utf-8'
    html = response.read()#,decode('utf-8')
    #print html 

    poemsoup = BeautifulSoup(html, 'html.parser')
    return poemsoup

fh = open('poems.txt','a')

#poemlists = ['/PoemIndex.aspx?dynasty=Tang&author=李白']
#本句测试用

poemcollection = []
n=0
person= 0
for poemlist in poemlists:
    
    checkpoint1 = time.clock()
    
    page = 0
    
    while 1 :
        html = view_poet(poemlist+'&type=All&page='+str(page))
        #print page
        
        try:
            if '下一页' in str(html):
                page = page + 1
                #print html
                poems = html.find_all('p')
                #print poems #通过<p>匹配诗文内容
                
                for i in poems:
                    poem = str(i)
                    if '<!-- -->' in poem:
                        #print poem
                        fmt = BeautifulSoup(poem,'lxml')
                        #print fmt
                        result = fmt.get_text()
                        final = result.split()                        
                        
                        for sentence in final:
                            #print type(sentence)
                            fh.write(sentence.encode('utf-8')+'\n\n')
                            n = n + 1    
                        continue                    
                        '''
                        下面是旧版代码，已经删除
                        poem = poem.replace('<','')
                        poem = poem.replace('-','')
                        poem = poem.replace(' ','')
                        poem = poem.replace('!','')
                        poem = poem.replace('>','')
                
                        #格式化诗词
                        poemcollection.append(str(poem))

                        fh.write(poem+'\n\n')
                        n = n+1
                        continue
                        '''
            
            else:   #最后一页也要写入
                poems = html.find_all('p')
                #print poems #通过<p>匹配诗文内容
                
                for i in poems:
                    poem = str(i)
                    
                    if '<!-- -->' in poem:
                        #print poem
                        fmt = BeautifulSoup(poem,'lxml')
                        #print fmt
                        result = fmt.get_text()
                        final = result.split()                        
                        
                        for sentence in final:
                            #print sentence
                            fh.write(sentence.encode('utf-8')+'\n\n')
                            n = n + 1    
                        continue
                break  
        
            
        except:
            continue
            
    checkpoint2 = time.clock()
    
    person = person + 1
    if (checkpoint2 - checkpoint1) > 5 or person%10 is 0:

        print '已抓取' + str(person) + '人'
        continue
                
'''
for i in poemlist:
    if 'class="title"' in i:
        poemcollection.append(i)
'''

fh.close()

endtime = time.clock() 
print '写入完毕，搜集到'+str(n)+'段唐诗'
print 'Totally spend' + str((endtime - starttime)) + 'seconds'  




