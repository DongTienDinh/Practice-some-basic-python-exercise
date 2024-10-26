n = str(input (" nhập vào dãy số nguyên n :"))
x=list()
tong=0
n = n.strip()
n = list(n)
for i in n:
    if i.isnumeric():
        x.append(i)
        tong+=int(i)
print (" + ".join(x),end=" = ")
print (tong)


