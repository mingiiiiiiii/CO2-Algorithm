import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
a.sort()
for i in range(n):
    print(a[i][0], a[i][1])
