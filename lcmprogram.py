# Calculating LCM

print('Enter Numerator of 1st value ')
first_numerator = int(input())
print('Enter Denominator of 1st value ')
first_denominator = int(input())
print('Enter Numerator of 2nd value ')
second_numerator = int(input())
print('Enter Denominator of 2nd value')
second_denominator = int(input())

cal_num_one = cal_num_two = cal_deno = 0    

cal_deno = first_denominator * second_denominator 
cal_num_one = cal_deno / first_denominator * first_numerator
cal_num_two = cal_deno / second_denominator * second_numerator
answer = (cal_num_one + cal_num_two) /cal_deno
print('Answer is {}'.format(answer))