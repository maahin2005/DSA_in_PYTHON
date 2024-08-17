# FIBONACCI SERIES: 0 1 1 2 3 5 8 13 21 ........

def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

ans = fib(4)
print(ans)