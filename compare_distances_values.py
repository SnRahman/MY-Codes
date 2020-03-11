first_value_feet = int(input('1st value Feet(s) : '))
first_value_inches = int(input('1st value Inche(s) : '))

second_value_feet = int(input('2nd value Feet(s) : '))
second_value_inches = int(input('2nd value Inche(s) : '))

if first_value_feet > second_value_feet:
    print('Greater Value is : {} Feets {} Inches'.format(first_value_feet,first_value_inches))
elif first_value_feet == second_value_feet:
    if first_value_inches > second_value_inches:
        print('Greater Value is : {} Feets {} Inches'.format(first_value_feet,first_value_inches))
    elif first_value_feet == second_value_feet:
        print("Both Values are same : {} Feets {} Inches and {} Feets {} Inches"
            .format(first_value_feet,first_value_inches,second_value_feet,second_value_inches))
    else:
        print('Greater Value is : {} Feets {} Inches'.format(second_value_feet,second_value_inches))
else:
    print('Greater Value is : {} Feets {} Inches'.format(second_value_feet,second_value_inches))