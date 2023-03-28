# 1912943 고주희
# 1번을 해보세요!
def binary(n):
    count = 1
    while n > 1:
        count = count +1
        n = n // 2
    return count


# 2번을 해보세요!
n = int(input())
    
# 출력합니다!
print(binary(n))