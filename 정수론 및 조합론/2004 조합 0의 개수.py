import sys

def find_two(x):
    k = 0
    while x != 0:
        x = x // 2
        k += x
    return k

def find_five(x):
    k = 0
    while x != 0:
        x = x // 5
        k += x
    return k

# 팩토리얼 이용 안하고 팩토리얼 연산 중 2와 5의 개수만 찾기 
# ex) 8! 에서 2의 개수 : 8보다 작은 2의 배수 4개 + 2^2의 배수 2개 (8 // 2^2) + 2^3의 배수 1개 (8 // 2^3)
# 2^2의 배수에 있는 2의 개수 1개씩 + 2^3의 배수에 있는 2의 배수 1개씩 + 2의 배수 = 7
  
n, m = map(int, sys.stdin.readline().split())
ans = min(find_five(n) - find_five(n-m) - find_five(m), find_two(n) - find_two(n-m) - find_two(m))
print(ans)        
