def print_heading(symbol,mul,heading):
	print(symbol * mul)
	print(heading)
	print(symbol * mul)

#functio that convert decimal to binary
def decimal_binary(decimal):
    binary = list()
    while(decimal >=2):
        if decimal%2 != 0:
            binary.append(1)
        else:
            binary.append(0)
        decimal = decimal//2
    binary.append(decimal)
    return binary

def main():
    #heading
    print_heading('*',30,'Decimal to Binary Convertor')

    #Take input
    number = int(input('Enter a Decimal Number to get its Binary : '))
    
    #call Functon
    binary = decimal_binary(number)
    
    for i in binary:
        print(i,end='')

if __name__ == "__main__":
    main()