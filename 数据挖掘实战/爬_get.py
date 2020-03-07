import requests

url = 'http://www.wuxiph.com/index.html'
strhtml = requests.get(url)
print(strhtml.text)



