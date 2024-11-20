#Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không?
# Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
dem=0
x=0
n= (input("Nhập vào một list số nguyên: "))
n=n.strip().split(" ")
n=list(map(int,n))
for i in range (len((n))):
    if i==(len(n)-1):
        break
    else:
        z=(n[i+1])-(n[i])
    if z==x:
        dem+=1
    x=z
if dem==(len(n)-2):
    print ("Vậy dãy số bạn vừa nhập là một cấp số cộng")
    print (f"Công sai của list số là {z}")
else:
    print ("None")
