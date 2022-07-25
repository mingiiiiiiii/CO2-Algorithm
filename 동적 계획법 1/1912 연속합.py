import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * len(a)
dp[0] = a[0]
for i in range(1, len(a)):
    dp[i] = max(a[i], a[i] + dp[i-1])
print(max(dp))
