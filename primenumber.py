print('#' * 40)
print('Check the given number is prime or not')
print('#' * 40)

i = int(input('Enter Number : '))

if (i == 1 or i == 3 or i == 5):
	print('{} IS a prime number'.format(i))
elif(i == 0 or i == 4):
	print('{} Not a prime number'.format(i))
else:
	if i%2 != 0 and i%3 != 0 and i%5 != 0:
		print('{} : Prime Number'.format(i))
	else:
		print('{} : Not a prime number'.format(i))