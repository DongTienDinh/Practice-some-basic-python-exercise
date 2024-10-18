n = int (input ("Nhập vào sỗ nguyên n: "))
i=n
demle=0
demchan=0
dem=0
while n >0:
    if n%2==0:
        demchan+=1
    else:
        demle+=1
    n= n//10
    dem+=1
print (f"Vậy {i} có {dem} chữ số")
print (f"{demchan} số chẵn và {demle} số lẻ")

