import sys
n = int(sys.stdin.readline())
list = [0] * 8001
sum = 0
for i in range(n):
    n2 = int(sys.stdin.readline())
    list[4000 + n2] += 1
    sum += n2
#산술평균
print(round(sum / n))

list2 = []
for i in range(8001):
    if list[i] != 0:
        for j in range(list[i]):
            list2.append(i - 4000)
#중앙값
if len(list2) == 1:
    print(list2[0])
else:
    print(list2[(n//2)])

#최빈값
n3 = max(list)
list3 = []
for i in range(8001):
    if list[i] == n3:
        list3.append(i)
if len(list3) == 1:
    print(list3[0] - 4000)
else:
    print(list3[1] - 4000)

#범위
print(list2[n-1] - list2[0])
