
a = 12345
b = 9

digits_of_a = []
digits_of_b = []
cal = []

def parsing_digits(value,list_to_store ):
    while value % 10 != 0  or value !=0:
        digit = value % 10
        remaining = int(value/10)
        list_to_store.append(digit)
        #print('Value {} and remaing {}'.format(digit ,remaining))
        value = remaining

def check_value(i,value):
    length = len(str(i))
    if length >= 16:
        temp = i % 10000000000000000
        i = int(i / 10000000000000000)
        parsing_digits(temp,value)
        check_value(i,value)
    else:
        parsing_digits(i,value)

def Reverse(lst):
    lst.reverse()
    return lst

check_value(a,digits_of_a)
check_value(b,digits_of_b)

print(digits_of_a)
print(digits_of_b)

for i in digits_of_b:   
    carry = 0
    for d in digits_of_a:
        temp1 = d * i
        temp1 = temp1 + carry
        if temp1 > 9:
            cal.append(temp1 % 10) 
            carry = int(temp1 /10)
        else:
            cal.append(temp1)
    cal.append(carry)

print(Reverse(cal))


