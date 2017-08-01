from bs4 import BeautifulSoup

import urllib.request
page=urllib.request.urlopen('http://mops.twse.com.tw/mops/web/ajax_t163sb04?encodeURIComponent=1&step=1&firstin=1&off=1&TYPEK=otc&year=106&season=02')
soup=BeautifulSoup(page.read().decode('utf-8','ignore'))
table = soup.find("table", { "class" : "hasBorder" })

rows = table.findChildren(['tr'])

for row in rows:
    print(row.text)
   
