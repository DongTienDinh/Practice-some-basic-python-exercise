#Nhập vào một list số nguyên L,
# hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
n=input("Nhập vào một list số nguyên: ")
n=n.strip().split(' ')
n=list(map(int,n))
dem=0
z=[]
for i in range (len(n)):
    for j in range (i):
        if n[i] > n[j]:
            dem+=1
        if dem==(i):
            z.append(n[i])
    dem=0
print(f"Có tất cả {len(z)}")
print (f"Vậy các số {z} thỏa mãn điều kiện")
