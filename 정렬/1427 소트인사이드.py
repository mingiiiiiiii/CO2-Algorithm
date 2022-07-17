n = input()
n1 = []
for i in range(len(n)):
    n1.append(int(n[i]))
n1.sort()
n3 = "".join(map(str, n1))
print(int(n3))
