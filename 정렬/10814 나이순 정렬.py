n = int(input())
a = []
for _ in range(n):
    a.append(input().split())
a = sorted(a, key = lambda x : int(x[0]))
for i in range(n):
    print(a[i][0], a[i][1])
