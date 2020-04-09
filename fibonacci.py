def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

#Recursive function
def fib_recursive(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


for n in range(1, 11): # testing
    print(n, "->", fib(n))
