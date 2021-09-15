# link bài tập: https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456
# bài 1
def bai1():
    for x in range(2000,3000):
        if x % 7 == 0:
            if x % 5 != 0:
                print(x,',',end = '')

# bài 2 
print(' Nhap so can tinh giai thua :', end = '')
n = int(input())
def bai2():
    x = 0
    kq = 1
    for x in range(n):
        x += 1
        kq = kq * x
    print(' Ket qua :',kq)

while n != 0:
    bai2()
    print(' Nhap so can tinh giai thua :',end = '')
    n = int(input())