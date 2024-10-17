a= int (input ("Nhập vào số nguyên a: "))
dem=0
for i in range (1,a+1):
    if a%i==0:
        dem+=1
if dem == 2:
    print (f"{a} là một số nguyên tố")
else:
    print (f"{a} không phải là số nguyên tố")