print('*' * 30)
print('Calculate the power')
print('*' * 30)

base = int(input("Enter the Number : "))
power = int(input("Enter the Power : "))
result = 1

for i in range(0,power):
  result *= base

print("Result is {}".format(result))