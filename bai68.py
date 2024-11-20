#Nhập vào một list số nguyên L,
# hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
n=input("Nhập vào một list số nguyên: ")
n=n.strip().split(' ')
n=list(map(int,n))
i=n.index(max(n))
j=n.index(min(n))
n[i],n[j]=n[j],n[i]
print("Giá trị lớn nhất và giá trị nhỏ nhất đã được đổi vị trí cho nhau trong chuỗi:")
print(n)
