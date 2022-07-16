import sys
n, m = map(int, sys.stdin.readline().split())
dict1 = {}
for i in range(n):
    dict1[sys.stdin.readline().rstrip()] = i
b = list(dict1.keys())
for i in range(m):
    a = sys.stdin.readline().rstrip()
    try:
        a = int(a)
    except:
        print(dict1[a] + 1)
    else:
        print(b[a-1])
