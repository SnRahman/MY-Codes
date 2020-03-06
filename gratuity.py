print('#' * 40)
print('Calculate the Gratuity')
print('#' * 40)

duration = 43
start_salary = 36000
anual_increment = 15000
gratuity = 0

for i in range(1,duration+1):
    if i % 13 == 0:
        start_salary += anual_increment
    gratuity += start_salary
print('Months : {} Current salary : {} Gratuity : {}'.format(i,start_salary,gratuity))
    

