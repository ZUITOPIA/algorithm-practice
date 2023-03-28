# 1912943 고주희
# 1번을 해보세요!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(factorial(n))