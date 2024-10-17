n = int (input ("Mời các bạn nhập n: "))
dem = 0
for i in range (n+1) :
    if i == n:
        dem+=i
        print (i,"=",dem)
    else:
        print (i,end=" + ")
        dem+=i