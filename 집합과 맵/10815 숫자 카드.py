import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dict1 = {}
for i in range(n):
    dict1[a[i]] = i
m = int(sys.stdin.readline())
a1 = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    if a1[i] in dict1:
        a1[i] = 1
    else:
        a1[i] = 0
for i in range(m):
    print(a1[i], end = ' ')
