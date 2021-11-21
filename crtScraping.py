# -*- coding: utf-8 -*-
import sys

import requests
import requests_cache
import lxml.html as lh
import pandas as pd

from bs4 import BeautifulSoup

url = 'https://crt.sh/?O=Google'
insto = requests_cache.CachedSession('myCache').get(url)

#print(insto.content)

soup = BeautifulSoup(insto.content, 'html.parser')

#for i in range(2):
#  print(soup.find_all('td',class_='outer')[i])

tables = soup.select(".outer table tr")

results = []
for i in range(1,10):
  print(list(tables[i])[9].get_text())
#print(list(tables[1]))
#print(list(list(soup.select(".outer table tr"))[2])[9].get_text())



#print(soup.prettify())

#myml = list(soup.children)[2]

#myml2 = list(myml.children)[3]

#print(list[myml2.children])

#url = 'https://crt.sh/?O=Apple+Inc'

#resi = requests_cache.CachedSession('myCache').get('https://crt.sh/?O=Apple+Inc')

#print(resi)
#page = requests.get(url)

#doc = lh.fromstring(page.content)

#tr_elements = doc.xpath('//tr')

#print(type(tr_elements[1].text_content()))

#tr_elementse = list(tr_elements)
#tr_elementse = tr_elements.pop(0)
#tr_elementse = tr_elements.pop(0)

#outF = open("myOutFile.txt", "w")
#for t in tr_elements[:15]:
#    outF.write(str(t.text_content()))

#myitems = []
#myitems.append(tr_elements)
#print(len(myitems))
#print([type(T) for T in tr_elements[:15]])


#col=[]
#i=0
#for t in tr_elements[2]:
#    i+=1
#    name=str(t.text_content())
#    print('%d:"%s"'%(i,name))
#    col.append((name,[]))

#print(tr_elements.text_content[2:10])

#for j in range(3, len(tr_elements)):
#    T = tr_elements[j]
#
#    i = 0
#
#    for t in T.iterchildren():
#        data=t.text_content()
#        if i>0:
#            try:
#                data = int(data)
#            except:
#                pass
#        col[i][1].append(data)
#        i+=1

#print([len(C) for C in col])

#Dict = {title:column for (title,column) in col}
#df= pd.DataFrame(Dict)

#print(df.head())
