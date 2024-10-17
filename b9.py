a = int (input ("Nhập vào số nguyên a: "))
b= int (input ("Nhâp vào số nguyên b: "))
dem=0
print (f"Ước chung của {a} và {b} bao gồm: ")
if a > b:
    z=b
else:
    z=a
for i in range (1,z+1):
    if a%i==0 and b%i ==0 :
        dem+=1
        print (i,end=" ")
print ()
print (f"Vậy {a} và {b} có {dem} ước chung")
