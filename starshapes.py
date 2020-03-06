
print('#' * 40)
print('Make patern of stars using loop')
print('#' * 40)

limit = 5
symbol = '*'

print("Shape 1")
for i in range(limit):
  for j in range(limit):
	  print(symbol, end ='')
  print(end = '\n')


print("Shape 2")
for i in range(limit):
  for j in range(limit,i,-1):
	    print(symbol,end='')
  print(end = '\n')

print("Shape 3")
for i in range(limit):
  for j in range(i+1):
	    print(symbol,end='')
  print(end = '\n')

print("Shape 4")
for i in range(limit+1):
  for j in range(limit,i,-1):
	    print(end =' ')
  for j in range(i):
      print('*',end ='')
  print(end='\n')

print("Shape 5")
for i in range(limit+1):
  for j in range(i):
	    print(end =' ')
  for j in range(limit,i,-1):
      print('*',end ='')
  print(end='\n')


print("Shape 6")
for i in range(limit+1):
  for j in range(limit,i,-1):
	    print(end =' ')
  for j in range(i):
      print('*',end ='')
  for j in range(i-1):
      print('*',end ='')
  print(end='\n')

print("Shape 7")
for i in range(limit):
  for j in range(limit,i,-1):
	    print(end =' ')
  for j in range(i):
      print('*',end ='')
  for j in range(i-1):
      print('*',end ='')
  print(end='\n')
for i in range(limit):
  for j in range(i):
	    print(end =' ')
  for j in range(limit,i,-1):
      print('*',end ='')
  for j in range(limit-1,i,-1):
      print('*',end ='')
  print(end='\n')
