import sys

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if ww[a][b][c]:
        return ww[a][b][c]
    if a < b and b < c:
        ww[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return ww[a][b][c]
    else:
        ww[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return ww[a][b][c]

ww = [[[0]*21 for _ in range(21)] for _ in range(21)] #리스트 표현식 사용

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    else:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
