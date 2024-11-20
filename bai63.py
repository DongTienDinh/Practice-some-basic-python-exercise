#Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện:
# có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận.
# Nếu L không tồn tại giá trị như vậy thì in ra - 1
dem=0
z=[]
n= (input("Nhập vào một list số nguyên: "))
n=n.strip().split(" ")
n=list(map(int,n))
for i in range (len(n)-2):
    if n[i+1]==n[i]*n[i+2]:
        dem+=1
        z.append(i+2)
if dem>=1:
    print (f"số cần tìm nằm ở vị trí số {z} của list")
else:
    print ("List số không tồn tại giá trị như vậy")
    print (-1)