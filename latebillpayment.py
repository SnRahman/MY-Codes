print('#' * 40)
print('Bill Late payment')
print('#' * 40)

starting_bill = 6565
current_bill = 6565 * 5
surcharger = current_bill * 0.12
current_bill = current_bill - surcharger

print('current bill is: {}'.format(current_bill))

