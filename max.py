print('#' * 40)
print('Find the max number form input')
print('#' * 40)

num = 0
max_number = 0

for i in range(1,6):
	num = int(input('Enter the {} number : '.format(i)))
	if num > max_number:
		max_number = num

print('Max Number is : {}'.format(max_number))