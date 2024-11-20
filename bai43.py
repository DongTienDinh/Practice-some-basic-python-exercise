#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
# Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
def gia_tri_trung_binh(x,y):
    dem=0
    tong=0
    for i in range (y):
        tong+= int(x[i])
        dem+=1
    return f" Giá trị trung bình của {y} giá trị đầu của {x} là {tong/dem}"
x=(input("Nhập một list số nguyên: "))
x=x.strip().split(" ")
while True:
    y= int (input ("Nhập một số nguyên: "))
    if y < len(x):
        break
z=gia_tri_trung_binh(x,y)
print (z)
