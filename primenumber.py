print('#' * 40)
print('Check the given number is prime or not')
print('#' * 40)

num = int(input('Enter the number : '))

check = 0
for i in range(2,num+1):
	for j in range(num, 1,-1):
		if i * j == num:
			check  += 1
if check > 0:
  print('Not a prime number')
else:
  print('Is a prime number')