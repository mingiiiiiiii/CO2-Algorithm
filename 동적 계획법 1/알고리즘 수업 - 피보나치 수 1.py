def fib(x):
    dp = [0] * (x+1)
    dp[1], dp[2] = 1, 1
    global cnt
    cnt = 0
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1
    return dp[x]

n = int(input())
print(fib(n), cnt)
