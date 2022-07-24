import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * (n+6)      # n이 6미만일 때 오류 방지
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6,n+1):
        dp[i] = dp[i-5] + dp[i-1]
    print(dp[n])
    
