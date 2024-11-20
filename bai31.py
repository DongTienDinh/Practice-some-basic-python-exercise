#Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list,
# số lẻ về cuối list và các phần tử 0 nằm ở giữa
n=input("Nhập vào một list số nguyên: ")
n=n.strip().split(' ')
n=list(map(int,n))
c=[]
l=[]
khong=[]
for i in (n):
    if i%2==0:
        c.append(i)
    elif i==0:
        khong.append(i)
    else:
        l.append(i)
print('list sau khi lọc nhận được l:')
print(c+khong+l)
