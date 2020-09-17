
def fib(n):    
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def list_fib(n):
    return [fib(i) for i in range(n)] #list comprehension

#print(list_fib(5))

L1 = [2, 4, 6]
L2 = [5, 3, 7]
L3 = [i for i in map(min, L1, L2)] #map
L4 = [i for i in map(lambda x,y: x*y, L1, L2)] #lambda
print(L4)

sum = lambda x,y: x+y
print(sum(2,6))
        