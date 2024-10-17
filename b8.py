a = int (input ("Nhập vào số nguyên a: "))
dem=0
print (f"Ước của {a} bao gồm: ")
for i in range (1,a+1):
    if a%i==0:
        dem+=1
        print (i,end=" ")
print ()
print (f"Vậy {a} có {dem} ước")
