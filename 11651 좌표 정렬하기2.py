import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
b = sorted(a, key = lambda x : (x[1],x[0]))
for i in range(n):
    print(b[i][0], b[i][1])
