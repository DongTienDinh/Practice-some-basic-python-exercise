"""
n = int (input (" Nhâp vào số nguyên n: "))
i=n
z=list()
dem=tong=0
while n > 0:
    x= n%10
    if n <10:
        print (x,end= " ")
    else:
        print (x, end = " + ")
    dem+=1
    tong+=x
    n = n//10
print ()
print (f"= {tong}")
print (f"Vậy số {i} có {dem} chữ số và tổng các chữ số là {tong}")
"""
#Cách 2
n = str(input("Nhập vào một số nguyên n: "))
so=0
for i in n:
     so+=int(i)
print (f" Vậy {n} có tổng các chữ số là {so}")
