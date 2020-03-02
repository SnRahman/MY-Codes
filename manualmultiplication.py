
a = 12345678901234567890
b = 12345678901234567890

digits_of_a = []
digits_of_b = []
rows = []

#parsing digists from variable to list
def parsing_digits(value,list_to_store ):
    while value % 10 != 0  or value !=0:
        digit = value % 10
        remaining = int(value/10)
        list_to_store.append(digit)
        value = remaining

#after 16 digits from decimal point, values goes in exponent power. to avoid such thing divide the
#value before 16 digits
def check_value(i,value):
    length = len(str(i))
    if length >= 16:
        temp = i % 10000000000000000
        i = int(i / 10000000000000000)
        parsing_digits(temp,value)
        check_value(i,value)
    else:
        parsing_digits(i,value)

#Reverse the list
def Reverse(lst):
    lst.reverse()
    return lst

#call the functions to store the values from variable to list
check_value(a,digits_of_a)
check_value(b,digits_of_b)


#Multiplication 
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

final_result = []
addition = base = carry = 0


#Performaing the final addition
while len(rows) > 0:
    if rows[0] == []:
        rows.remove(rows[0])

    for i in range(0,len(rows)):
        if len(rows[i] ) == 0 :
            print('row is : {}'.format(rows[i]))
            print('index is : {}'.format(i))    
            pass
        else: 
            addition += rows[i].pop()
    addition += carry
    print('addition is {}'.format(addition))
    print(rows)
    carry = 0
    if addition > 9:
        base = addition % 10 
        carry = int(addition /10)
        final_result.append(base)
    else:
        final_result.append(addition)
        carry = 0
    addition = 0

reverse_list = Reverse(final_result)

#Removing the extra Zeros
while reverse_list[0] == 0:
    print('call')
    reverse_list.remove(reverse_list[0])



print('Final Result is: {}'.format(reverse_list))
print(a*b)



