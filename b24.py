n = int (input (" Nhập vào giá trị của n: "))
s=a=dem=tong=0
z=[]
while tong<n:
    s+=(a+1)
    tong+=s
    z.append(s)
    dem+=1
tong=tong-s
z.pop(len(z)-1)
print ("S(k)= ",end="")
print (" + ".join(map(str,z)), f" = {tong}")
print (f" Vậy k = {dem-1} thì S(k)= {tong} lớn nhất nhỏ hơn {n} ")