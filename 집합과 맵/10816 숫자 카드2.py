import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dict1 = dict()   #dict1 = {}
for i in range(n):
    try:
        dict1[a[i]] += 1
    except:
        dict1[a[i]] = 1
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    try:
        print(dict1[b[i]], end = ' ')
    except:
        print(0, end = ' ')
