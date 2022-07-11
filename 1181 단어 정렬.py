n = int(input())
a = []
for _ in range(n):
    a.append(input())
a = list(set(a))
a = sorted(a, key = lambda x : (len(x),x))
for i in range(len(a)):
    print(a[i])
