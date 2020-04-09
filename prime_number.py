def isPrime(num):
    check = 0
    for i in range(2,num):
       if num %i == 0:
           check += 1
    if check > 0:
        return False
    else:
        return True
        
for i in range(1, 40):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()