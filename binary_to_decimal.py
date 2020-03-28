def print_heading(symbol,mul,heading):
	print(symbol * mul)
	print(heading)
	print(symbol * mul)

#convert binary to decimal
def binary_to_decimal(lst):
    mul = len(lst) - 1
    decimal = 0

    for i in range(mul,-1,-1):
        if lst[i] == '1':
            decimal += 2**i
        else:
            pass

    return decimal

#store binary number to a list
def convert_to_list(num):
    binary = list()
    for i in num:
        binary.append(i)
    return binary

def main():
    #heading
    print_heading('*',30,'Binar to Decimal Convertor')

    #Take Input
    number = input('Enter Binary to get its Decimal Number : ')

    #call functions
    binary_list = convert_to_list(number)
    decimal = binary_to_decimal(binary_list)
    
    print(decimal)


if __name__ == "__main__":
    main()