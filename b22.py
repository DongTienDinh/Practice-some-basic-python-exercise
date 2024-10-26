n=int (input ("Nhập vào một số nguyên A: "))
x=tong=0
y=1
z=[0, 1]
while tong <= n:
    tong = x+y
    z.append(tong)
    x=y
    y=tong
z.pop(int(len(z))-1)
print ("Dãy fibonacci có dạng là: ",end="")
print (", ".join(map(str,z)))
print (f"Số lớn nhất trong dãy fibonacci là {x} không vướt quá {n} số bạn đã nhập")
