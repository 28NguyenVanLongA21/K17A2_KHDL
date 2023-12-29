
import math
# def hàm
def f(x,n):
    return math.pow(math.pow(x,2)+1,n)
# gọi hàm
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
print("S=",f(x,n))