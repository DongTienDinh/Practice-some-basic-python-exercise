import math
print ("Chương trình kiểm tra số chính phương")
n = int (input ("Nhập vào một số nguyên: "))
if math.sqrt(n) == math.ceil(math.sqrt(n)):
    print ("Đây là số chính phương")
else:
    print ("Đây không phải là số chính phương")