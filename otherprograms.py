print('*' * 30)
print('Calculate The fee in Rupees')
print('*' * 30)

fee_in_pound = 300
fee_in_rupees = 300 * 192.21
tranaction_fee = fee_in_rupees * 0.09
print(
    'Fee in Pound : {} \nTransaction Fee : {}\nFee in Rupees is {}:'
    .format(fee_in_pound,tranaction_fee,fee_in_rupees -tranaction_fee )
    )

#############################################
print('*' * 30)
print('Difference Between / and //')
print('*' * 30)

a = 6968
b = 21

#gives the values after decimals
print('/ gives the values after decimals : {}'.format(a/b))
#Ignore decimal values just give 
print('// Ignore the values after decimals : {}'.format(a//b))