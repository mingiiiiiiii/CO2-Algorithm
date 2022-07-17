import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(set(a))
b = sorted(b)
dic = {}
for i in range(len(b)):
    dic[b[i]] = i
for i in range(n):
    print(dic[a[i]], end = ' ')
#index 함수 사용하면 시간초과로 dict 
