#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
# Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L
def tim_so_nguyen_to(x,y):
    dem1=0
    dem2=0
    z=[]
    for i in range (y):
        for j in range (int(x[i])):
            if x[i])%j==0:
                dem1+=1
        if dem==2:
                dem2+=1
                z.append(x[i])
    return f"Vậy {y} kí tự đầu cảu {x} có {dem2} số nguyên tố và đó là {z} "
x=(input("Nhập một list số nguyên: "))
x=x.strip().split(" ")
while True:
    y= int (input ("Nhập một số nguyên: "))
    if y < len(x):
        break
z=tim_so_nguyen_to(x,y)
print(z)
