# 1912943 고주희
# 1번을 해보세요!
def slow_power(x, n) :
    result = 1.0
    for i in range(n):
        result = result * x
    return result


# 2번을 해보세요!
x = int(input())
n = int(input())

# 출력합니다!
print("억지기법(%d**%d) =" %(x, n), slow_power(x, n))
