import requests
from bs4 import BeautifulSoup
import os
def tieba():
	get_a = 1
	bs = 1
	name = 1
	for i in range(1,page+1):
		url = url_all+"?pn="+str(i)
		user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"
		headers = {"User-Agent":user_agent}
		print("正在发送第%d次get请求..."%(get_a))
		get_a += 1
		content = requests.get(url,headers=headers)
		print("状态码："+content.status_code)
		print("正在解析网页信息...当前次数%d"%(bs))
		bs += 1
		Soup = BeautifulSoup(content.text,"html.parser")
		all_img = Soup.find_all('img',class_='BDE_Image')
		for a in all_img:
			src = a["src"]
			img = requests.get(src,headers=headers)
			print("正在存储数据...")
			f = open(str(name)+'.jpg', 'ab')
			f.write(img.content) 
			f.close()
			name += 1
	print("爬取完毕！")
def File():
	path = pagename
	os.makedirs(os.path.join("F:\mzitu", path))
	os.chdir("F:\mzitu\\"+path)
	tieba()
if __name__ == '__main__':
	url_all = input("请输入需要爬取的贴吧URL：")
	page = int(input("请输入需要爬取帖子的页数："))
	pagename = input("请为存储信息的文件夹命名:")
	File()