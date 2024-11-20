#Người ta định nghĩa một list số nguyên được gọi là “dạng sóng”
# khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.
#Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không,
# nếu có thì ta in ra True, không có thì ta in False
l= input("Nhập vào một list số nguyên L: ")
l=l.strip().split(" ")
l=list(map(int,l))
dem=0
for i in range (len(l)-2):
    if all(x< l[i+1] for x in [l[i],l[i+2]]) or all (x> l[i+1] for x in[l[i],l[i+2]]):
        dem+=1
    else:
        print("False")
        break
if dem==(len(l)-2):
    print("Chuỗi bạn nhập vào là một chuỗi dạng sóng")
