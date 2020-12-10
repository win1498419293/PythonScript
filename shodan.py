# ! /usr/bin/env python
# coding:utf-8
import re
def readfile(txtfile):
    mobile={""}
    f=open(txtfile,"r",encoding="UTF-8")
    data=f.readlines()
    for line in data:
        li=line.split(',')
        for l in li:
            cont=re.compile(("1\d{10}"))
            id=re.compile("(\d{4,8})")
            ss=cont.findall(l)
            #print(ss)
            dd=id.search(l).group()
            for b in ss:
                mobile.add(b)
                print(dd+"："+b)
    return mobile
def WriteFile(newTxtfile,mobile):
    with open(newTxtfile,"a+")as f:
        for i in mobile:
            phion = "".join(i)
            f.write(str(phion)+'\n')
            #print(phion)
def main():
    txtfile = r"C:\Users\Administrator\Desktop\新建文件夹\text.xls"
    newtxtfile = r"C:\Users\Administrator\Desktop\新建文件夹\mobile.xls"
    mobile=readfile(txtfile)
    WriteFile(newtxtfile,mobile)
if __name__ == "__main__":
    main()


