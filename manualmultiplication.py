
a = 12345
b = 921

digits_of_a = []
digits_of_b = []
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

count = 0
for i in digits_of_b:   
    carry = 0
    rows.append([])
    for c in range(0,count):
        if(count == 0):
            pass
        else:
            rows[count].append(0) 

    #Multiply with values of A
    for d in digits_of_a:
        temp1 = d * i
        temp1 = temp1 + carry
        if temp1 > 9:
            rows[count].append(temp1 % 10) 
            carry = int(temp1 /10)
        else:
            rows[count].append(temp1)
            carry = 0
    if carry == 0:
        pass
    else:
        rows[count].append(carry)
    rows[count] = Reverse(rows[count])
    count+=1


print(digits_of_a)
print(digits_of_b)


for row in rows:
    print(row)

final_result = []
addition = base = carry = 0

while len(rows[0] )> 0 or len(rows[1] )> 0 or len(rows[2] )> 0:
    for i in range(0,len(rows)):
        if len(rows[i] ) == 0:
            pass
        else: 
            addition += rows[i].pop()
    addition += carry
    carry = 0
    if addition > 9:
        base = addition % 10 
        carry = int(addition /10)
        final_result.append(base)
    else:
        final_result.append(addition)
        carry = 0
    addition = 0

print('Final Result is: {}'.format(Reverse(final_result)))



