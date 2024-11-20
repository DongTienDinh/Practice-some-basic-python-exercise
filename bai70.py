#Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên,
# hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không,
# nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
# K[i/2] = L[i]*L[i+1] (với i chẵn)
n=input("Nhập vào một list : ")
n=n.strip().split(' ')
k=[]
for i in range (len(n)):
    if n[i].isnumeric():
        n[i]=int(n[i])
if len(n)%2==0:
    x=None
    for j in range (len(n)-1):
        if (type(n[j]) is str and type(n[j+1]) is int) or (type(n[j]) is int and type(n[j+1]) is str):
            x= True
        else:
            print (i)
            print ("List của bạn không phải là các chuỗi và số xe khẽ nhau 1")
            x=False
            break
    if x== True:
        for z in range (0,len(n),2):
            m=(n[z]*n[z+1])
            k.append(m)
else:
    print ("List của bạn không phải là các chuỗi và số xe khẽ nhau 2 ")
print ("Vậy từ list L ta tạo được list K mới là {}".format(k))
