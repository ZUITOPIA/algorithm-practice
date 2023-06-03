# 최장 공통 부분순서 (순환 구조)

# 1912943 고주희
# 1번을 해보세요!
def lcs_recur(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1+ lcs_recur(X, Y, m-1, n-1)
    else:
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n))


# 2번을 해보세요!
X = input()
Y = input()


# 출력합니다!
print("X = ", X)
print("Y = ", Y)
print("LCS(분할 정복)", lcs_recur(X , Y, len(X), len(Y)))
