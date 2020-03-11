print('#' * 40)
print('Calculate the provident fund')
print('#' * 40)

base_salary = 35000
pf = 35000 * 0.08
employed_duration = 39
total_pf = 0
interest = total_interest = 0

for i in range(1,40):
    total_pf += pf*2
    interest = total_pf * 0.06
    total_interest += interest
    total_pf += interest
    #print('Provident Fund of Months {} is : {} interest is : {}'.format(i,round(total_pf,),round(interest,)))

print('Provident Fund of 39 Months is : {} Total Interest is : {}'.format(round(total_pf,),round(total_interest,)))
