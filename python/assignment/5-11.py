# 피보나치 수열 (반복구조)

# 1912943 고주희
# 1번을 해보세요!
def fib_iter(n):
    if (n<2) : return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(fib_iter(n))