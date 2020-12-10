# coding:utf-8
import sys
import  re
def readname(txtfile):
    uname={""}
    f=open(txtfile,"r",encoding="UTF-8")
    data=f.readlines()
    for line in data:
        #for l in li:
        username=re.compile('user_login.*?user_em')
        un=username.findall(line)
        for b in un:
            uname.add(b)
    return uname
def Writename(newTxtfile,uname):
    with open(newTxtfile,"a+",encoding='utf-8')as f:
        for i in uname:
            phion = "".join(i)
            try:
                pp=phion.encode('utf-8').decode('unicode_escape')
                f.write(str(pp)+'\n')
                #print(phion)
            except:
               print("出错了",i)
            finally:
                f.write(str(phion) + '\n')
def main():
    c=''
    txtfile = r"C:\Users\Administrator\Desktop\新建文件夹\text.xls"
    newtxtfile = r"C:\Users\Administrator\Desktop\新建文件夹\uname.txt"
    uname=readname(txtfile)
    Writename(newtxtfile,uname)
if __name__ == "__main__":
    main()

