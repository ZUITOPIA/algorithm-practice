# 1912943 고주희
# 1번을 해보세요!
def factorial(n):
    # None이라고 되어있는 부분을 수정해보세요
    result = 1
    for k in range(n, 0, -1):
        result = result * k
    return result

# 2번을 해보세요!
n = int(input())
    
# 출력합니다!
print(factorial(n))