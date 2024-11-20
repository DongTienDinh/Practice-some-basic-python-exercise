#Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không
from typing import Any


def kiem_tra_so_armstrong(a):
    b = str(a)
    if len(b)==1:
        a = "00"+b
    if len(b)==2:
        a= "0"+b
    m = a
    b=str(a)
    tong = sum(int(i) ** len(b) for i in b)
    phep_tinh= "+".join(f"{i}^{len(b)}" for i in b)+ f"= {tong}"
    if tong == m:
        print (phep_tinh)
        return (f"{m} là số armstrong")
    else:
        print (phep_tinh)
        return (f"{m} không phải là số armstrong")

a=int (input ("nhập vào giá trị của a:"))
b= kiem_tra_so_armstrong(a)
print (b)

