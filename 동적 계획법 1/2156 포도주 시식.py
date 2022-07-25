import sys
n = int(sys.stdin.readline())
a= [0]
dp = [0] * (n+1)
for _ in range(n):
    a.append(int(sys.stdin.readline()))
dp[1] = a[1]
if n > 1:
    dp[2] = a[1] + a[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i], dp[i-1])
print(dp[n]) 
    
