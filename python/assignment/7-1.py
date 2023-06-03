# 피보나치 수열 (메모이제이션 이용)

# 1912943 고주희
# 1번을 해보세요!
def fib_dp_mem(n) :
    if (mem[n] == None):
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

# 2번을 해보세요!
n = int(input())

# 출력합니다!
mem = [None] * (n+1)
print('Fibonacci(%d) = '%n, fib_dp_mem(n))