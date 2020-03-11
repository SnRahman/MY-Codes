

def cal_int_fractional(num):
    length_of_num = len(str(num))
    int_num = round(num // 1,)
    lenght_of_int = len(str(int_num))
    decimal_num = round(num % 1,length_of_num-lenght_of_int)

    return int_num , decimal_num


def calculation(f1,i1,f2,i2):
    if f1 > f2:
        print('Greater Value is : {} Feets {} Inches'.format(f1,i1))
    elif f1 == f2:
        if i1 > i2:
            print('Greater Value is : {} Feets {} Inches'.format(f1,i1))
        elif f1 == f2:
            print("Both Values are same : {} Feets {} Inches and {} Feets {} Inches"
                .format(f1,i1,f2,i2))
        else:
            print('Greater Value is : {} Feets {} Inches'.format(f2,i2))
    else:
        print('Greater Value is : {} Feets {} Inches'.format(f2,i2))

def main():
    first_value = input('1st value Feet(s) and Inches : ')
    first_value_cal = cal_int_fractional(float(first_value))
    first_value_feet = first_value_cal[0]
    first_value_inches = first_value_cal[1]

    second_value = input('1st value Feet(s) and Inches : ')
    second_value_cal = cal_int_fractional(float(second_value))
    second_value_feet = second_value_cal[0]
    second_value_inches = second_value_cal[1]

    calculation(first_value_feet,first_value_inches,second_value_feet,second_value_inches)

if __name__ == "__main__":
    main()
