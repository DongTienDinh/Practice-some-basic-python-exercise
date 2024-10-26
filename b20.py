def C_sang_F (c):
    return  (c*(9/5))+32
def F_sang_C(f):
    return (f-32)*(5/9)
print ("Nhập lựa chọn bạn muốn quy đổi:  ")
print ("Đổi độ C sang F thì bấm phím 1")
print ("Đổi độ F sang C thì bấm phím 2")
p= int (input ("Nhập số: "))
if  p==1:
    x=int (input ("Nhập độ C: "))
    c = C_sang_F(x)
    print (f"Vậy {x} độ C đổi thành {c} độ F")
elif p==2:
    x = int(input("Nhập độ F: "))
    f = F_sang_C(x)
    print(f"Vậy {x} độ F đổi thành {f} độ C")


