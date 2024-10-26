
def kiem_tra_mat_khau(x):
    h=t=s=db=0
    for i in (x):
        if i.isnumeric() :
            s+=1
        elif i.isupper():
            h+=1
        elif i.islower():
            t+=1
        else:
            db+=1
    return h, t, s, db

print (" Chương trình kiểm tra mật khẩu mạnh ")
n = str (input ("Nhập vào mật khẩu của bạn : "))
n=n.strip()
n=list(n)
while True:
    h, t, s, db = kiem_tra_mat_khau(n)
    if h>=1 and t>=1 and s>=1 and db>=1 and len(n)>=6:
        print("Mật khẩu của bạn đã đủ mạnh")
        break
    else:
        print ("Warning!Mật khẩu của bạn chưa đủ mạnh")
        n = str(input("Nhập lại mật khẩu của bạn : ")).strip()
        n=list(n)




