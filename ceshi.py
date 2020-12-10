import  re
import requests
import bs4
from bs4 import BeautifulSoup
from multiprocessing import Process
def gethtmltext():
    #构造请求头信息
    header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Referer": "http://localhost/finecms.com/index.php?s=/admin/login",
    }
    with open(r"C:\Users\Administrator\Desktop\新建文件夹\eru8.txt", "a+", encoding="UTF-8")as  f:
        for post in range(30000,40000):
            url = r"http://39.96.127.36"
            url+=(":"+str(post))
            print(url)
            try:
                req = requests.get(url, headers=header,timeout=30)
                req.raise_for_status()
                req.encoding = req.apparent_encoding
                print("{}端口可以打开".format(post))
                f.write(str(url) + "\n")
                break
            except:
               print("{}端口无法打开".format(post))

def main():
    gethtmltext()
if __name__ == '__main__':
    main()