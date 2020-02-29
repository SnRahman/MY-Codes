
a = 12345
b = 921

digits_of_a = []
digits_of_b = []
row = []
rows = []

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

count = 1
for i in digits_of_b:   
    carry = 0
    row.clear()

    for c in range(1,count):
        row.append(0) 
    count+=1

    #Multiply with values of A
    for d in digits_of_a:
        temp1 = d * i
        temp1 = temp1 + carry
        if temp1 > 9:
            row.append(temp1 % 10) 
            carry = int(temp1 /10)
        else:
            row.append(temp1)
            carry = 0
    if carry == 0:
        pass
    else:
        row.append(carry)
    
    #print(row)
    #rows.append(str(row))
    rows.append(str(row))


print(digits_of_a)
print(digits_of_b)


for row in rows:
    print(row)
    



