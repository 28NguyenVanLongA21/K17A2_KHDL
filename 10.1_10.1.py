
import datetime
d=int(input("Nhập ngày:"))
m=int(input("Nhập tháng:"))
y=int(input("Nhập năm:"))
my_birthday=datetime.date(y,m,d)
print("Sinh nhật của tôi vào ngày:",my_birthday.strftime("%d-%m-%y"))
#Kiểm tra xem có phải năm nhuận không?
import calendar
print("Năm này là năm:",calendar.isleap(y))
#Cho biết đây là thứ mấy?
import calendar
print("Ngày này rơi vào thứ:",calendar.weekday(y,m,d))
#Cho biết tháng có bao nhiêu ngày
import calendar
print("Tháng này có:",calendar.monthrange(y,m))