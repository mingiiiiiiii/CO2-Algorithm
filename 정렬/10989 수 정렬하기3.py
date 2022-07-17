import sys

n = int(input())
list = [0] * 10000
for i in range(n):
    list[int(sys.stdin.readline()) - 1] += 1
for i in range(10000):
    if list[i] != 0:
        for j in range(list[i]):
            print(i+1)
