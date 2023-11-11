import math
a = float(input("Nhập độ dài cạnh A: "))
b = float(input("Nhập độ dài cạnh B: "))
c = float(input("Nhập độ dài cạnh C: "))
p = (a + b + c) / 2
dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Diện tích của tam giác là: {dien_tich}")