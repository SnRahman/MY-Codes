#To Chek the leap year

print('Enter the year')
year = int(input())

if year % 4 == 0 and year % 100 != 0: 
    print('is a leap year')    
elif year % 400 == 0:
    print('is a leap year')
else:
    print('not a leap year')
