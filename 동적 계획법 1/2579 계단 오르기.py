import sys
n = int(sys.stdin.readline())
stp = []
dp = [0] * n
for _ in range(n):
    stp.append(int(sys.stdin.readline()))
if n == 1:
    print(stp[0])
elif n == 2:
    dp[0] = stp[0]
    print(stp[1] + dp[0])
else:
    dp[0] = stp[0]
    dp[1] = stp[1] + dp[0]
    dp[2] = max(stp[0] + stp[2], stp[1] + stp[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + stp[i-1] + stp[i], dp[i-2] + stp[i])
    print(dp[n-1])
