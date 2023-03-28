# 1912943 고주희
# 1번을 해보세요!
def binary_digits(n):
    if n <= 1:
        return 1
    else:
        return 1+binary_digits(n // 2)


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(binary_digits(n))