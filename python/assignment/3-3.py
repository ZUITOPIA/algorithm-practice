# 1912943 고주희
# 1번을 해보세요!
def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]:
            j = j + 1
        if j == m:
            return i
    return -1

# 2번을 해보세요!
T = input()
P = input()

# 출력합니다!
print(string_matching(T, P))