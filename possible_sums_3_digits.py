mylist = [1,3,5,7,9,11,13,15]
rezult = list()
count = 0

for i in range(len(mylist)):
    for j in range(i,len(mylist)):
        for k in range(j,len(mylist)):
            if mylist[i] + mylist[j] + mylist[k] == 30:
                print(mylist[i] , mylist[j] , mylist[k])
            else:
                digit_sum = mylist[i] + mylist[j] + mylist[k] 
                print(digit_sum)
                if digit_sum not in  rezult:
                    rezult.append(digit_sum)
                count += 1
print(count)
print(len(rezult))
print(rezult)