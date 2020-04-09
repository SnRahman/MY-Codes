print('#' * 40)
print('Calculaing factorial of given number')
print('#' * 40)

num = int(input('Enter the number : '))

factorial = 1
for i in range(num+1):
    for j in range(1,i+1):
        factorial *=j
    if i != num:
        factorial = 1
print('factorail of {} is {}'.format(num,factorial))

#recursive function
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

print(factorialFun(10))
