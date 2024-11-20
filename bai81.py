#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a.
# Hãy tìm và trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất,
# a = 2 thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)
def tim_gia_tri_lon(x,y):
        z=sorted(x)
        x.sort
        x= list(reversed(x))
        return f"Số lớn thứ {y} của list {z} là {x[y-1]}"
x=(input("Nhập một list số nguyên: "))
x=x.strip().split(" ")
while True:
    y= int (input ("Nhập một số nguyên: "))
    if y < len(x):
        break
z=tim_gia_tri_lon(x,y)
print(z)

