def print_heading(symbol,mul,heading):
	print(symbol * mul)
	print(heading)
	print(symbol * mul)

def prime_number(num):
	check = 0
	for i in range(2,num+1):
		for j in range(num, 1,-1):
			if i * j == num:
				check  += 1
	if check > 0:
		return 0
	else:
		return 1 

def main():
	print_heading('*',40,'Calculate prime Number after Given Number')
	num = int(input('Enter Number : '))
	i = num 

	count = 0
	while count !=1:
		i = i + 1
		count = prime_number(i)
	
	print('Prime Bigger than {} is {}'.format(num,i))

if __name__ == "__main__":
	main()
	