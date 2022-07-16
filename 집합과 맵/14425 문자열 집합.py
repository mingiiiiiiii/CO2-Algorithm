import sys
n, m = map(int, sys.stdin.readline().split())
dict1 = {}
for i in range(n):
    dict1[sys.stdin.readline()] = i
num = 0
for i in range(m):
    if sys.stdin.readline() in dict1:
        num += 1
print(num)
