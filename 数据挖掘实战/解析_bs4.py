import requests
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li')
print(data)
print('soup类型是：\n', type(soup))
print('data类型是：\n', type(data))
for item in data:
    # print(item)
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
    print(result)




