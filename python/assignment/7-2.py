# 피보나치 수열 (테이블화 이용)

# 1912943 고주희
# 1번을 해보세요!
def fib_dp_tab(n) :
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]	


# 2번을 해보세요!
n = int(input())

# 출력합니다!
print('Fibonacci(%d) = '%n, fib_dp_tab(n))
