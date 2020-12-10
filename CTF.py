import json
import  re
import requests
import bs4
from bs4 import BeautifulSoup
from multiprocessing import Process
def gethtmltext(url):
    #构造请求头信息
    header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    }
    try:
        #自定义请求信息
        req=requests.get(url,headers=header)
        req.raise_for_status()
        req.encoding=req.apparent_encoding
        return req.text
    except:
        return  "连接失败"
def fillUnivList(req,sevefile):
    soup=BeautifulSoup(req,'lxml')
    text = soup.find_all('h3')
    for item in text:
        result = {
            'title': item.get_text(),
            'link': item.find('a').get('href')
        }
        with open(sevefile,"a+",encoding='utf-8')as f:
            f.write(json.dumps(result,ensure_ascii=False)+"\n")
            f.close
        print(result)
    return True
def run(name):
    print('%s runing' % name)
def main():
    uinfo=[]
    wd="intitle:xiaomi"
    pn="50"
    url = 'http://www.baidu.com/s?wd='+wd+'&pn='+'pn'
    req= gethtmltext(url)
    sevefile=r'E:\1.txt'
    f=fillUnivList(req,sevefile)
if __name__ == '__main__':
    main()