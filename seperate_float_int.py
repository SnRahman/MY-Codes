num = 99868769.45868

length_of_num = len(str(num))
int_num = round(num // 1,)
lenght_of_int = len(str(int_num))
decimal_num = round(num % 1,length_of_num-lenght_of_int)

print('Integer Part is : {} Fractional Part is : {}'.format(int_num,decimal_num))

