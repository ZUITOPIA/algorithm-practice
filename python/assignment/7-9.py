# LCS 테이블에서 LCS를 추적하는 알고리즘

# 1912943 고주희
# 동적 계획법으로 최장 공통 부분순서를 구하는 함수
def lcs_dp(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :
                L[i][j] = 0	
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # 함수 lcs_dp_traceback(X, Y, L)를 호출해요!
    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n] 

# 1번을 해보세요!
def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j-1] and v > L[i-1][j] and v > L[i-1][j-1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs

        elif v == L[i][j-1] and v > L[i-1][j] : j -= 1
        else: i -= 1
    return lcs

# 2번을 해보세요!
X = input()
Y = input()

# 출력합니다!
print("X = ", X)
print("Y = ", Y)
lcs_dp(X, Y)