def isYearLeap(year):
    if year >=1882:
        if year%4 != 0:
            return False
        elif year%100 != 0:
            return True
        elif year%400 !=0:
            return False
        else:
            return True
    else:
        print('Not within the Gregorian calendar period')

def daysInMonth(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year) and month == 2:
        return 29
    else:
        return days[month-1]
        
def dayOfYear(year, month, day):
    count = 0
    for i in range(1,month):
        days = daysInMonth(year,i)
        count += days
    count += day
    
    return count
    
    
print(dayOfYear(2000, 12, 31))