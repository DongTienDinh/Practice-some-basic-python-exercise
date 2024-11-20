#Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
def gia_tri_lon_nhat(a):
    a = a.strip()
    a = a.split(" ")
    a = list(map(int, a))
    b=0
    for i in (a):
        if i >b:
            b=i
    return b
a=(input ("Nhập vào một list giá trị của a: "))
x= gia_tri_lon_nhat(a)
print (f"Giá trị lớn nhất của list này là {x}")
