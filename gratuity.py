print('#' * 40)
print('Calculate the Gratuity')
print('#' * 40)

duration = 43
start_salary = current_salary= 36000
anual_increment = 15000

for i in range(1,duration+1):
    if i % 12 == 0:
        current_salary += anual_increment

annual_duration = duration/12
gratuity = annual_duration * current_salary    
print('Months : {} Current salary : {} Gratuity : {}'.format(i,current_salary,gratuity))
