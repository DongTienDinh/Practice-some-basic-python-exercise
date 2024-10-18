n = int (input ("Nhâp vào số nguyên n: "))
i=n
dem=0
while n > 0:
    n= n//10
    dem+=1
print ("Vậy {} có {} chữ số".format(i,dem))#cách 1
print (f"Vậy {i} có {dem} chữ số")#cách 2