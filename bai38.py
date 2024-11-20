#Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
def kiem_tra_so_nguyen_to(a):
    dem = 0
    for i in range (1,a+1):
        if a%i==0:
            dem+=1
    if dem==2:
        return (f"{a} là số nguyên tố")
    else:
        return(f"{a} không phải là số nguyên tố")
a= int (input ("Nhập vào một giá trị của a: "))
b= kiem_tra_so_nguyen_to(a)
print (b)
