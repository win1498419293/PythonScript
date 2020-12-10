# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


'''def gethtml(url):
    header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'bcolor=; font=; size=; fontcolor=; width=',
    'Host':'www.biqukan.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'https://www.biqukan.com/42_42882/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
    try:
        # 自定义请求信息
        req = requests.get(url, headers=header)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return "连接失败"
def getlist(html):
    soup=BeautifulSoup(html,'html.parser')
    title = soup.find_all('h1')
    content=soup.find_all('div',{'class':'showtxt'})
    print(content)
def main():
    url='http://www.biqukan.com/42_42882/14586139.html'
    html=gethtml(url)
    getlist(html)
if __name__ == '__main__':
    main()'''

if __name__ == '__main__':
    target = 'https://www.biqukan.com/42_42882/14586139.html'
    req = requests.get(url=target)
    print(req.text)