#Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list
def chuoi_ngan_nhat(x):
    b=len(x[0])
    for i in range(len(x)):
        if len(x[i]) < b:
            b=len(x[i])
            c=i
    return f"Vậy chuỗi ở vị trí \"{str(x[c])}\" có {b} kí tự ít nhất trong list"

x=str(input ("nhập vào một list dược ngăn cách bởi dấu phẩy: "))
x=x.strip().split(",")
a= chuoi_ngan_nhat(x)
print (a)
