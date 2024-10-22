import math
a = float (input ("Nhap he so cho bien a: "))
b = float (input ("Nhap he so cho bien b: "))
c = float (input ("Nhap he so cho bien c: "))
print (f"Phương trình của bạn có dạng là {a}x^2 + {b}x + {c} = 0")
delta = b**2 - 4*a*c
if a != 0:
    if delta >0:
        x1= (-b-math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print (x1)
        print (x2)
    elif delta == 0:
        x1 = x2 = -b/(2*a)
        print ("x1=x2=",x1)
    elif delta < 0:
        print ("Phương trình vô nghiệm")
else:
    print ("Phương triình có một nghiêệm x=",-c/b)
