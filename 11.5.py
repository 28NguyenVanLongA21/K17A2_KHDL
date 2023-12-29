
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
#In ra tất cả các số nguyên tố trong list
list_NT=[]
for i in list:
        if i==2:
               list_NT.append(i)
        for j in range(2,i):
                if i%j==0 or i<=1:
                        list_NT=list_NT
list_NT.append(i)
print("List số nguyên tố:",list_NT)
#In các phần tử âm:
list_am=[]
list_duong=[]
for i in list:
        if i<0:
                list_am.append(i)
        elif i>0:
                list_duong.append(i)
print("Các phần tử âm trong list:",list_am)
print("TBC âm=",sum(list_am)/len(list_am))
print("Các phần tử dương trong list:",list_duong)
print("TBC dương=",sum(list_duong)/len(list_duong))
print("Giá trị max trong list:",max(list))
print("Giá trị min trong list:",min(list))
list.sort()
print("List sắp tăng dần:",list)


                        