import sys
n = int(sys.stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + dp[i][0]
    dp[i][i] = dp[i-1][i-1] + dp[i][i]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
print(max(dp[n-1]))
