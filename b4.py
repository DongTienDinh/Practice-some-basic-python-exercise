print (" Nhập độ dài của 3 cnahj của một tam giác: ")
a = float (input("Nhập độ dài cạnh a: "))
b = float (input ("Nhập độ dài cạnh b: "))
c = float (input ("Nhập độ dài cạnh c: "))
if (a+b)>c and (b+c)>a and (a+c)>b and all( x>0 for x in [a, b, c]):
    print ("Ba cạnh bạn nhập vào có thể tạo thành một tam giác")
else:
    print ("Ba cạnh của bạn nhập vào không tạo được một tam giác")
