import sys
a = int(sys.stdin.readline())
if a == 1:
    real = int(sys.stdin.readline())
    print(real*real)
else:
    real = list(map(int, sys.stdin.readline().split()))
    real.sort()
    print(real[0] * real[-1])
