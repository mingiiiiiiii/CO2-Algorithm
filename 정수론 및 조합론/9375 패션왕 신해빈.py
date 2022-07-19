import sys
n = int(sys.stdin.readline())
for _ in range(n):
    tmp = {}
    k = int(sys.stdin.readline())
    for _ in range(k):
        a, b = map(str, sys.stdin.readline().split())
        if b not in tmp:
            tmp[b] = 1
        else:
            tmp[b] += 1
    tmp2 = list(tmp.values())
    ans = 1
    for tmp2s in tmp2:
        ans *= (int(tmp2s) + 1)
    print(ans-1)        
