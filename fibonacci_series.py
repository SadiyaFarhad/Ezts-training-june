#Program to find fibonacci_series
def fib(n):
    fib_series=[]
    a,b=0,1
    for _ in range(n):
        fib_series.append(a)
        a,b=b,a+b
    return fib_series

print(fib(10))
#OUTPUT : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
