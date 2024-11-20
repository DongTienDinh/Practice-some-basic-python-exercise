#Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
def sosanh(a,b):
    if a>b:
        for i in range (11):
            print (f"{a} x {i} = ",a*i)
    else:
        for i in range (11):
            print (f"{b} x {i} = ",b*i)
a= int (input(" Nhập vào giá trị của a: "))
b= int (input(" Nhập vào giá trị của b: "))
while a > 10 or b > 10 :
    print ("Bạn đã nhập sai cú pháp hãy nhập lại: ")
    a = int(input(" Nhập vào giá trị của a: "))
    b = int(input( " Nhập vào giá trị của b: "))
sosanh(a,b)

