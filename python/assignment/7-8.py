# 최장 공통 부분순서 (동적 계획법)

# 1912943 고주희
# 1번을 해보세요!
def lcs_dp(X , Y):
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]


# 2번을 해보세요!
X = input()
Y = input()

# 출력합니다!
print("X = ", X)
print("Y = ", Y)
print("LCS(동적 계획)", lcs_dp(X , Y) )
