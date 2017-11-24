# import requests
# from bs4 import BeautifulSoup
# resp = requests.get("https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion")
# try:
#     soup = BeautifulSoup(resp.text, "lxml")
# except:
#     soup = BeautifulSoup(resp.text, "html5lib")
# print(soup.get("span"))
# print(soup.prettify())

# import mechanize

# # ブラウザをエミュレート
# browser = mechanize.Browser()
# response = browser.open("https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion")
# #HTMLを表示
# print(response.read())

# from pyquery import PyQuery

# pq = PyQuery(url='https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion')
# print(pq)

# from urllib.request import Request, urlopen

# req = Request('https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# import requests
# from bs4 import BeautifulSoup


# url = "https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion"
# headers = {'User-Agent':'Mozilla/5.0'}
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")

# print(soup.span)
# print(soup.prettify())


# import urllib.request
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# f = opener.open("https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion")
# f.read()

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen


url = 'https://cookpad.com/ng/search/egg%20onion%20carot?event=search.suggestion'#まずはurlをぶち込む
req = Request(url)
response = urlopen(req)#開け！url
html = response.read()#htmlを読み込んでぶち込む
soup = BeautifulSoup(html, "lxml")#ここでBeautifulsoupの出番だぁっ
# contents = soup.find_all(id = 'contents') #今回抜き出したいタグ
# print(contents)
