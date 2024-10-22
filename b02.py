nam = int (input ("Nhap nam: "))
thang = int (input("Nhap thang: "))
if nam % 4 ==0:
    if thang == 2:
        print (f'Tháng {thang} năm {nam} có 29 ngày vì là năm nhuận')
else:
    if thang ==2:
         print(f'Tháng {thang} năm {nam} có 28 ngày vì không phải là năm nhuận')
if thang in [1,3,5,7,8,10,12]:
    print(f'Tháng {thang} năm {nam} có 31 ngày')
if thang in [4,6,9,11]:
    print (f'Tháng {thang} năm {nam} có 30 ngày')

