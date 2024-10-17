print ("Số lẻ dương nhỏ hơn 100 là: ")
dem=0
for i in range (0,100):
    if i % 2 !=0:
        dem+=1
        print(i,end=" ")
print()
print (f"Trong đây có {dem} số dương lẻ")
