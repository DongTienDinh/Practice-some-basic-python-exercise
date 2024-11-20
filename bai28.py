#Người ta định nghĩa một list số nguyên là list chẵn lẻ,
# nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ

#Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
n=input("Nhập vào một list số nguyên: ")
n=n.strip().split(" ")
n=list(map(int,n))
dem=0
for i in range (len(n)-1):
    if (n[i]+n[i+1])%2!=0 :
        dem+=1
if dem==(len(n)-1):
    print("Vậy list số nguyên bạn nhập vào là môt list chẵn lẻ")
else:
    print("Vậy list số nguyên mà bạn nhập vào không phải là một list chẵn lẻ")
