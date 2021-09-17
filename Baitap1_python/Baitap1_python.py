# link bài tập: https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
# bài 1
def bai1():
    for x in range(2000,3000):
        if x % 7 == 0:
            if x % 5 != 0:
                print(x,',',end = '')

# bài 2 
def bai2():
    print(' Nhap so can tinh giai thua :', end = '')
    n = int(input())
    def tinh():
        x = 0
        kq = 1
        for x in range(n):
            x += 1
            kq = kq * x
        print(' Ket qua :',kq)

    while n != 0:
        tinh()
        print(' Nhap so can tinh giai thua :',end = '')
        n = int(input())

# bài 3
def bai3():
    print(' Nhap so nguyen :', end = '')
    n = int(input())
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    print(d)

# bài 4
def bai4():
    print(' Nhap so nguyen :',end = '')
    n = int(input())
    l = list()
    for i in range(n):
        l.append(input(' Nhap so :'))
    t = tuple(l)
    print(l)
    print(t)

# bài 9
import math
def bai9():
    import math
    c=50
    h=30
    value = []
    items=[x for x in input("Nhập giá trị của d: ").split(',')]
    for d in items:
        value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    print (','.join(value)

