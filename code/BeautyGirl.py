import requests
from bs4 import BeautifulSoup
import os
# 目标URL地址
all_url = "http://www.mzitu.com/all"
# 浏览器请求头
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent":user_agent}
# 获取目标URL网页内容
start_html = requests.get(all_url,headers = headers)
Soup = BeautifulSoup(start_html.text,"html.parser")
all_a = Soup.find("div",class_="all").find_all("a")
for a in all_a:
	title = a.get_text()
	href = a["href"]
	html = requests.get(href,headers = headers)
	html_soup = BeautifulSoup(html.text,"html.parser")
	try:
		max_span = html_soup.find('div',class_="pagenavi").find_all('span')[-2].get_text()
	except AttributeError:
		print('NoneType01')
		for page in range(1,int(max_span)+1):
			page_url = href + '/' + str(page)
			img_html = requests.get(page_url, headers=headers)
			img_Soup = BeautifulSoup(img_html.text, "html.parser")
			try:
				img_url = img_Soup.find('div', class_='main-image').find('img')['src']
				name = img_url[-9:-4]
				img = requests.get(img_url, headers=headers)
				f = open(name+'.jpg', 'ab')
				f.write(img.content)
				f.close()
			except AttributeError:
				print('NoneType02')