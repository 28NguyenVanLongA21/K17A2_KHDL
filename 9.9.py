
import math
def dien_tich_hinh_tron(r):
        return math.pow(r,2)*3.14
r=float(input("Nhập bán kính r:"))
print("Diện tích hình tròn S=",dien_tich_hinh_tron(r))

def chu_vi_hinh_tron(r):
        C=2*r*3.14
        return C
r=float(input("Nhập bán kính r:"))
print("Chu vi hình tròn C=",chu_vi_hinh_tron(r))

#Tính diện tích, chu vi hình chữ nhật
def dien_tich_hinh_chu_nhat(a,b):
        S=a*b
        return S
a=float(input("Nhập chiều dài a:"))
b=float(input("Nhập chiều rộng b:"))
print("Diện tích hình chữ nhật S=",dien_tich_hinh_chu_nhat(a,b))

def chu_vi_hinh_chu_nhat(a,b):
        P=(a+b)*2
        return P
a=float(input("Nhập chiều dài a:"))
b=float(input("Nhập chiều rộng b:"))
print("Chu vi hình chữ nhật P=",chu_vi_hinh_chu_nhat(a,b))