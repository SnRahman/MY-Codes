#To Chek the leap year

print('Enter the year')
year = int(input())

if year % 4 == 0 and year % 100 != 0: 
    print('is a leap year')    
elif year % 400 == 0:
    print('is a leap year')
else:
    print('not a leap year')

#2nd mathod
year = int(input("Enter a year: "))

if year >=1882:
    if year%4 != 0:
        print('Common year')
    elif year%100 != 0:
        print('Leap year')
    elif year%400 !=0:
        print('Common year')
    else:
        print('Leap year')
else:
    print('Not within the Gregorian calendar period')