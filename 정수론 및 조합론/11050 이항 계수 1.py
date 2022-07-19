import sys

def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x-1)
    
n, k = map(int, sys.stdin.readline().split())
a = factorial(n) // (factorial(n-k) * factorial(k))
print(a)
