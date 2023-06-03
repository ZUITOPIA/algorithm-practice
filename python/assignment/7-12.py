# 편집 거리 (동적 계획법, 메모이제이션 사용)

# 1912943 고주희
# 1번을 해보세요!
def edit_distance_mem(S, T, m, n, mem): 
    if m == 0: return n
    if n == 0: return m

    if mem[m-1][n-1] == None:
        if S[m-1] == T[n-1]:
            mem[m-1][n-1] = edit_distance_mem(S,T,m-1,n-1,mem)

        else: 
            mem[m-1][n-1] = 1 + \
                min(edit_distance_mem(S,T,m,n-1,mem),
                edit_distance_mem(S,T,m-1,n,mem),
                edit_distance_mem(S,T,m-1,n-1,mem))
    return mem[m-1][n-1]


# 2번을 해보세요!
S = input()
T = input()


# 출력합니다!
m = len(S)
n = len(T)
print("문자열:", S, T)
mem = [[None for _ in range(n)] for _ in range(m)] 
dist = edit_distance_mem(S, T, m, n, mem)
print("편집거리(메모이제이션)=", edit_distance_mem(S, T, m, n, mem))