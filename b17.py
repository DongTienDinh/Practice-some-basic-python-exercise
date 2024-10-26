n = str(input ("Nhập vào chuỗi  n: "))
p=n
s=h=t=db=0
n=list(n)
for i in (n):
    if i.isnumeric() :
        s+=1
    elif i.isupper():
        h+=1
    elif i.islower():
        t+=1
    else:
        db+=1
print (f' Vậy dãy {p} có :')
print (f"{s} số")
print (f"{h} chữ hoa")
print (f"{t} chữ thường")
print (f"{db} kí tự đặc biệt")