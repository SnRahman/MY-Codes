print('#' * 40)
print('Finding factors of given number')
print('#' * 40)

factors = []
num = int(input('Enter the number : '))
print('Factors of {} are '.format(num))
for i in range(1,num):
    if num % i == 0:
        temp = round(num/i,)
        if i and temp in factors:
            pass
        else:
            factors.append(i)
            print('{} x {} =  {}'.format(i,temp,num))
            