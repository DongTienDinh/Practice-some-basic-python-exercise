#Nhập vào một list L có các phần tử là chuỗi
# (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
#Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
n = input ("Nhập một chuỗi các kí tự và khoảng trắng: ")
n=(x.strip() for x in n.split(","))
n=list(map(str,n))
z=0
for i in range (len(n)):
    x=n[i].count(" ")+1
    if x>z:
        z=x
        m=i
print ("Vậy trong list L thì chuỗi {} có nhiều từ nhất là {} và nằm ở vị trí số {}".format(n[i],z,m+1))

