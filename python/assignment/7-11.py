# 편집 거리 (순환 구조, 분할 정복)

# 1912943 고주희
# 1번을 해보세요!
def edit_distance(S, T, m, n):
    if m == 0: return n
    if n == 0: return m 

    if S[m-1] == T[n-1]:
        return edit_distance(S, T, m-1, n-1)

    return 1 + min(edit_distance(S,T,m, n-1), edit_distance(S,T,m-1,n), edit_distance(S,T,m-1,n-1))


# 2번을 해보세요!
S = input()
T = input()


# 출력합니다!
m = len(S)
n = len(T)
print("문자열:", S, T)
print("편집거리(분할정복)=", edit_distance(S, T, m, n))

