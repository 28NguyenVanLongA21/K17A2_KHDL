a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tổng số hạng vừa nhập là: ",S)