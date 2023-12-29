#Bài 9.5: Xây dựng phương thức tính (2)
import math
# def hàm
def f(x,n):
    return math.pow((math.pow(x,2) + x + 1),n)+math.pow((math.pow(x,2) - x + 1),n)
# gọi hàm
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
print("A=",f(x,n))