#Bài 9.8: Viết hàm kiểm tra 1 số có phải là số hoàn hảo không?
#def hàm
def kiem_tra_so_hoan_hao(n):
        S=0
        for i in range(1,n):
               if n%i==0:
                S+=i
        if S==n:
                print("Số hoàn hảo")
        else:
                print("Không phải là số hoàn hảo")
                return
#gọi hàm
n=int(input("Nhập n:"))
print("n:",kiem_tra_so_hoan_hao(n))