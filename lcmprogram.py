print('*' * 40)
print('Performing calculatons on Fractions')
print('*' * 40)

first_numerator = int(input('Enter Numerator of 1st value : '))
first_denominator = int(input('Enter Denominator of 1st value : '))
second_numerator = int(input('Enter Numerator of 2nd value : '))
second_denominator = int(input('Enter Denominator of 2nd value : '))
operator = input('Enter the Operator : ')

cal_num_one = cal_num_two = cal_deno = cal_nume = 0    

if operator == '+': 
    cal_deno = first_denominator * second_denominator 
    cal_num_one = cal_deno / first_denominator * first_numerator
    cal_num_two = cal_deno / second_denominator * second_numerator
    cal_nume = round(cal_num_one + cal_num_two,)
elif operator == '-':
    cal_deno = first_denominator * second_denominator 
    cal_num_one = cal_deno / first_denominator * first_numerator
    cal_num_two = cal_deno / second_denominator * second_numerator
    cal_nume = round(cal_num_one - cal_num_two,)
elif operator == '*':
    cal_nume = first_numerator * second_numerator
    cal_deno = first_denominator * second_denominator
elif operator == '/':
    cal_nume = first_numerator * second_denominator
    cal_deno = first_denominator * second_numerator
else:
    print('Wrong Operator')
print('Answer is {} / {}'.format(cal_nume,cal_deno))
