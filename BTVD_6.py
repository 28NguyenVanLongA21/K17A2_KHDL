#1.1
print('**  ** ****** **   **   ******')
print('**  ** **     **   **   **  **')
print('****** ****** **   **   **  **')
print('**  ** **     **   **   **  **')
print('**  ** ****** **** **** ******')
#1.3
print('tên hàng: sữa hộp vinamilk')
print('số lượng: 5')
print('đơn giá: 25000')
print('tiền phải trả:150000')
#1.4
a = float(input('nhập độ dài cạnh a:'))
b = float(input('nhập độ dài cạnh b:'))
c = float(input('nhập độ dài cạnh c:'))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('diện tích tam giác là:', s)