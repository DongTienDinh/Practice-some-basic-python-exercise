n = str (input ("Nhập vào mọt dãy 3 số nguyên: "))
z= n
n=n.split(",")
tong=0
for i in n:
    tong+=int(i)
print (f" Tổng của {z} là {tong}")
