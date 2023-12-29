#Bài 9.6: Viết hàm kiểm tra số nguyên tố
#def hàm
def kiem_tra_so_nguyen_to(n):
    if n<=1:
        print ("Hãy nhập số tự nhiên > 1 để xét")
    else:
        for i in range(2, n):
            if n % i==0:
                print (n,"không phải là số nguyên tố - FALSE")
            break
        else:
            print(n,"là số nguyên tố - TRUE")
            return
# gọi hàm
n=int(input("Nhập n: "))
print("n:",kiem_tra_so_nguyen_to(n))