#Nhập vào một list L có các phần tử là chuỗi.
#Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
n= input (" Nhập vào một chuỗi kí tự: ")
n = (x.strip() for x in n.split (","))
n=list(map(str,n))
z=0
for i in (n):
    for j in range (len(i)):
        if i[j].isupper():
            j =int(j)
        if j > z:
            z=j
            l=i


print ("Vậy trong list này có chuỗi \"{}\" có vị trí kí tự in hoa lớn nhất".format(l))
