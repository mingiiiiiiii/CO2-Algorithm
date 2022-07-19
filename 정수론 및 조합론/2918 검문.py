import sys
import math
def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
gcd = num[1] - num[0].  #초기값
for i in range(2,n):
    gcd = GCD(gcd, num[i] - num[i-1])    # num[i] - num[i-1]들의 최대공약수 구하기
num2 = []
for i in range(2, int(math.sqrt(gcd))+1):  # 최대공약수의 약수 구하기
    if gcd % i == 0:
        num2.append(i)
        if gcd/i != i:
            num2.append(int(gcd/i))
num2.append(gcd)
num2.sort()
for num2s in num2:
    print(num2s , end = ' ')
