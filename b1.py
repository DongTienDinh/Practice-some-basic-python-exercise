toan = float (input ("Nhap diem toan: "))
van = float (input ("Nhap diem van: "))
anh = float (input ("Nhap diem anh: "))
while all(0>=x and x>=10 for x in [toan, van, anh]):
    print ("Điểm của bạn đã nhập sai cúi pháp. Mời bạn nhập lại điểm!")
    toan = input("Nhap diem toan: ")
    van = input("Nhap diem van: ")
    anh = input("Nhap diem anh: ")
dtb = ( toan + van + anh) / 3
if dtb >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5:
    print("Học sinh giỏi (HSG)")
elif dtb >= 6.5 and toan >= 5 and van >= 5 and anh >= 5:
    print("Học sinh khá (HSK)")
elif dtb >= 5 and toan >= 3.5 and van >= 3.5 and anh >= 3.5:
    print("Học sinh trung bình (HSTB)")
elif dtb >= 3.5 and toan >= 2 and van >= 2 and anh >= 2:
    print("Học sinh yếu (HSY)")
else:
    print("Học sinh kém (HSK)")