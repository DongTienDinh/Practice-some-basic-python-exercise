n =  int (input ("Nhập vào số nguyên n: "))
i=n
dem = 0
while True:
    if n%2==0:
        n=n/2
        if n!=1:
            dem+=1
        else:
            print(f"Số {i} có dạng 2 mũ {dem}")
            break
    else:
        print (f"Số {i} không có dạng 2 mũ k")
        break

