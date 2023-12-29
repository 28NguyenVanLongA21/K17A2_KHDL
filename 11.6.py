
list_inch=[74,74,72,72,73,69,69,71,76,71]
#Đổi inch sang mét
list_meters=[]
for i in list_inch:
          i=i*0.0254
          list_meters.append(i)
print("Đối inch sang mét ta được:",list_meters)
#In ra 3 chiều cao đầu tiên, 3 chiều cao cuối cùng
list_temp_1=list_inch[:3]
list_temp_2=list_inch[7:]
print("3 chiều cao đầu tiên là",list_temp_1)
print("3 chiều cao cuối cùng là",list_temp_2)
#In ra chiều cao trung bình, chiều cao lớn nhất, chiều cao nhỏ nhất
m=sum(list_inch)/len(list_inch)
print('Chiều cao trung bình là:',round(m,2))
print('Chiều cao lớn nhất là:',max(list_inch))
print('Chiều cao nhỏ nhất là:',min(list_inch))
#Sắp xếp list theo thứ tự tăng dần
list_inch.sort()
print("Thứ tự tăng dần:",list_inch)
#Sắp xếp list theo thứ tự giảm dần
list_inch.sort()
list_inch.reverse()
print("Thứ tự giảm dần:",list_inch)

