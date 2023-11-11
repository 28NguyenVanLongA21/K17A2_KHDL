#7.1
x= input('nhập x:')
s = 1 + x + x^3/3 + x^5/5
print("s=", s)
#7.2
result = 1+2
print('result',result)
original_result = result
result = result - 1
print ('result', result)
original_result = result
result = result * 2
original_result = result
print ('result=', result)
result = result ** 3
original_result = result
print('result=', result)
result = result + 8
original_result = result
print('result', result)
result = result % 7
original_result = result
print('result', result)
result = result // 2
original_result = result
print('result', result)
#7.3
result = 5
print ('result=',result)
result -= 1
print('resut=', result)
result += 3
print('result', result)
result = - result
print('result', result)
result = True 
print('not result=', not result)
#7.4
x= 10
y= 4
print('x = %d, y = %d'%(x,y))
equivelence = x==y
print('x==y is', equivelence)
equivelence = x!=y
print("x!=y is",equivelence)
equivelence = x>y
print('x>y is',equivelence)
x= 8
y= 9
print('x = %d, y = %d'%(x,y))
equivelence = x>=y
print('x>=y is', equivelence)
equivelence = x<y
print('x<y is',equivelence)
equivelence = x<=y
print('x<=y is', equivelence)
#7.5
x = 15 
y = 12
print('Binary of x =', bin (x), ', Binary of y =', bin(y))
print('x & y = ', bin(x & y))
print('x / y =', bin(x | y))
print('x ^ y =', bin(x ^ y))
print('~x =', bin(~x) )
print('x << 2 =', bin (x << 2))
print('x >> 2 =', bin (x >> 2))
#7.6
x = True
y = False
print ('x and y :', x and y)
print ('x or y :', x or y)
print ('not x :',not x)
print ('x is y :', x is y)
print ('x is not y', x is not y)
