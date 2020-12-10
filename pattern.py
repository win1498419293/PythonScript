import  re
def ReadFile(txtfile):
    f=open(txtfile,"r")
    data=f.readlines()
    new_data=set(data)
    return new_data
def WriteFile(newTxtfile,new_data):
    with open(newTxtfile,"a+",encoding='utf-8')as f:
        phion="".join(new_data)
        f.write(str(phion) + '\n')
        print(phion)
def main():
    txtfile=r"C:\Users\Administrator\Desktop\新建文件夹\新建文本文档.txt"
    newTxtfile=r"C:\Users\Administrator\Desktop\新建文件夹\mobile.txt"
    new_data =ReadFile(txtfile)
    WriteFile(newTxtfile,new_data)
main()