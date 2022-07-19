def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

import sys
n = int(sys.stdin.readline())
r = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    gcd = GCD(r[0], r[i])
    print('{}/{}'.format(int(r[0]/gcd), int(r[i]/gcd)))
