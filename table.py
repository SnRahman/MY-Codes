print('#' * 40)
print('Get table of a given number')
print('#' * 40)

num = int(input('Enter the number to get its table'))

for i in range(1,41):
	print('{} X {} = {}'.format(num,i,num*i))