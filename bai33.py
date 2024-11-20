#Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên,
# hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
n=input("Nhập vào một list : ")
n=n.strip().split(' ')
z=[]
m=[]
for i in (n):
    if i.isdigit():
        m.append(int(i))
    else:
        z.append(str(i))
m=min(m)
z=max(z,key=len)
print(f"Chuỗi có độ dài lớn nhất là {z}")
print (f"Số nguyên có giá trị nhỏ nhất là {m}")
