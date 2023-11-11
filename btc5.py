#BT1.1
print("**     **  ******  **      **     ******")
print("**     **  **      **      **     **  **")
print("*********  ******  **      **     **  **")
print ("**     **  **      **      **     **  **")
print("**     **  ******  ******* ****** ******")
#BT1.2
print('xin mời nhập dữ liệu')
x=float(input("nhập giá trị x:"))
y=float(input("nhập giá trị y:"))
tong = x+y
hieu = x-y
tich= x*y
thuong=x/y
print ('tổng của hai só', x, '+', y, '=', tong)
print ('hiệu của hai só', x, '-', y, '=', hieu)
print (' tich của hai só', x, '*', y, '=', tich)
print ('thương của hai só', x, '/', y, '=', thuong)
import math
can_bac_hai_x=math.sqrt(x)
print('căn bậc hai của', x, '=', can_bac_hai_x)
#BT 1.3
ten_hang= "sữa hộp vinamilk"
so_luong= 5
don_gia= 25000
bill = so_luong * don_gia
print('tên hàng:', ten_hang)
print('số lượng:',so_luong)
print('đơn giá:',don_gia)
print ('tiền phải trả:',bill)