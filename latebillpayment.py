print('#' * 40)
print('Bill Late payment')
print('#' * 40)

starting_bill = 6565
current_bill = 0
surcharger = 0

for i in range(1,6):
    current_bill += starting_bill 
    surcharger = current_bill * 0.12
    current_bill += surcharger
    #print('Bill for month {} is: {}'.format(i,current_bill))

print('current bill is: {}'.format(round(current_bill,)))
