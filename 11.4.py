
list=[]
x=int(input("Nhập giá trị:"))
list.append(x)
i=1
while i==1:
          y=int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không"))
          if y==1:
                  x=int(input("Nhập giá trị:"))
                  list.append(x)
          elif y==0:
                  break
print("list:",list)
#Tính tổng các giá trị của list
sum=0
for num in list:
        sum+=num
print("Tổng các giá trị trong list:",sum)
#Kiểm tra x có mặt trong list không? Số lần xuất hiện của số x (nếu có)
x=int(input("Nhập giá trị cần tìm:"))
find = x in list
if find=="True":
        print(x,"xuất hiện",list.count(x),"lần trong list")
#x có lớn hơn tất cả các số trong list không
for i in list:
        if i>x:
          print(x,"không lớn hơn tất cả các số trong list")
          break
new_list=[]
for i in list:
        if i>x:
               new_list.append(i)
print("Các số lớn hơn",x,"trong list:",new_list)

          



