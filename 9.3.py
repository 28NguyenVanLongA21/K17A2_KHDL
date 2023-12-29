
can_nang=float(input("Nhập cân nặng:"))
chieu_cao=float(input("Nhập chiều cao:"))
BMI=can_nang/(chieu_cao*chieu_cao)
if BMI<18.5:
          print("Gầy")
elif BMI>=18.5 and BMI<=24.9:
        print("Bình thường")
else:
        print("Thừa cân")
print("Chỉ số BMI của bạn:", BMI)