import sys

def factorial(x):
    if x < 2:
        return 1
    else:
        return x * factorial(x-1)
    
n = int(sys.stdin.readline())
N = str(factorial(n))
ans = 0
for i in range(len(N)-1,-1,-1):
    if int(N[i]) == 0:
        ans += 1
    else:
        break
print(ans)        
