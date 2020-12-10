import requests
import os
url="http://m10.music.126.net/20200310204342/6ca44f9d03fb71dd4b9b9c226940678f/ymusic/0b6b/ab8f/ab4a/乱乱唱.mp3"
root="D://0404//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("保存失败")
