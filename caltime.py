print('#' * 30)
print('Calculate time in minutes')
print('#' * 30)

seconds = int(input('Enter the seconds :'))
minutes = int(input('Enter the Minutes :'))
hours = int(input('Enter the Hours :'))

hours_in_minutes = hours * 60
sec_to_minuts = (seconds / 60)
total_min = minutes + hours_in_minutes + sec_to_minuts
print('Total Minutes are : {}'.format(total_min))
