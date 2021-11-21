# -*- coding: utf-8 -*-
import sys

import requests_cache

from bs4 import BeautifulSoup

url = 'https://crt.sh/?dNSName=google.com'
insto = requests_cache.CachedSession('myCache').get(url)

soup = BeautifulSoup(insto.content, 'html.parser')

tables = soup.select(".outer table tr")

print("***Sub Domains from Google ***")
for i in range(1,35):
  print(i,list(tables[i])[9].get_text())
