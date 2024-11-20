#Viết hàm đưa vào một list số nguyên và một số nguyên dương k.
# Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
def find_K_in_list(a,k):
    k=int(k)
    a = a.strip()
    a = a.split(" ")
    a = list(map(int, a))
    b=0
    for i in range (len(a)+1):
        if a[i] == k :
            return f"vậy {k} ở vị trí {i+1} trong list {a} "
    return -1

a=input ("Nhập vào một list số nguyên: ")
while True:
    k=(input ('Mời bạn nhập một số nguyên dương: '))
    if k.isnumeric():
        k=int(k)
        if k>0:
            break
        else:
            k = (input('Mời bạn nhập lại một số nguyên dương: '))


x=find_K_in_list(a,k)
print (x)