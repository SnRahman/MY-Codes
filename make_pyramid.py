blocks = int(input("Enter the number of blocks: "))

count = 0
height = 0

while count < blocks:
    if blocks - count > height: 
        height +=1
        count += height
        print("count: {} height: {} Blocks: {}".format(count,height,blocks))
    else:
        break
print("The height of the pyramid:", height)