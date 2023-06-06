# 공간으로 시간벌기 (동적계획법)

### 복습 : 축소 정복 기법의 하향식과 상향식

def factorial_recur(n): # 팩토리얼 (하향식 축소 정복 기법 예시) - 순환(재귀) 구조
    if n == 1:
        return 1
    else:
        return (n * factorial_recur(n-1))

def factorial_iter(n): # 팩토리얼 (상향식 축소 정복 기법 예시) - 반복 구조
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result

### 동적계획법의 하향식과 상향식

def fib_dp_mem(n): # 피보나치수열 (하향식 동적계획법 예시) - 메모이제이션 
    if (mem[n] == None):
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n] 

def fib_dp_tab(n): # 피보나치수열 (상향식 동적계획법 예시) - 테이블화
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

### 이항계수로 알아보는 - 분할 정복 vs 동적 계획법

def bino_coef_dc(n,k): # 이항계수 - 분할 정복 기법
    if k == 0 or k == n:
        return 1
    return bino_coef_dc(n-1, k-1) + bino_coef_dc(n-1, k)

def bino_coef_dp(n,k): # 이항계수 - 동적 계획법 : O(nk)
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

### 배낭채우기로 알아보는 - 분할 정복 vs 동적 계획법
def knapSack_bf(W, wt, val, n): # 배낭 채우기 - 분할 정복 기법 (많은 중복이 발생하는 단점)
    if n == 0 or W == 0 :
        return 0
    
    if (wt[n-1] > W):
        return knapSack_bf(W, wt, val, n-1)
    else:
        valWithout = knapSack_bf(W, wt, val, n-1)
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout)
    

def knapSack_dp(W, wt, val, n): # 배낭 채우기 - 동적 계획법 : O(nW)
    A = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for W in range(1, W+1):
            if wt[i-1] > W:
                A[i][W] = A[i-1][W]
            else:
                valWith = val[i-1] + A[i-1][W-wt[i-1]]
                valWithout = A[i-1][W]
                A[i][W] = max(valWith, valWithout)

    return A[n][W]

### 최장 공통 부분순서로 알아보는 - 분할 정복(순환 구조) vs 동적 계획법
def lcs_recur(X, Y, m, n):  # 최장 공통 부분순서 - 분할 정복 기법 (많은 중복이 발생하는 단점)
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recur(X, Y, m-1, n-1)
    else: 
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n))
    
def lcs_dp(X, Y): # 최장 공통 부분순서 - 동적 계획법
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] == L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]
    
### 최장 공통 부분순서 중 해당 문자열을 찾아내기
def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j-1] and L[i-1][j] and v > L[i-1][j-1]:
            # 현재 값이 가는 방향(서쪽, 북쪽, 북서쪽)에 있는 값보다 크면 북서쪽으로 한 칸 이동
            i -= 1
            j -= 1
            lcs = X[i] + lcs # 대각선(북서쪽)으로 이동할 때마다 나온 값을 쭉 저장 (그게 곧 해당 문자열)

        elif v == L[i][j-1] and  v > L[i-1][j] : j -= 1
            # 현재 값이 서쪽과 같고 북쪽보다는 크다면 서쪽으로 한 칸 이동
        else: i -= 1
            # 그 외의 경우 위로 한 칸 이동
    return lcs

### 최단 경로 문제

import copy
def shortest_path_floyd(vsize, W): # Floyd의 최단 경로 탐색 알고리즘 O(n^3)
    D = copy.deepcopy(W) # 배열의 주소값이 아닌 원소의 모든 값들을 다 복사할 수 있음
    # D = W 주소복사

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if (D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)

### 편집 거리로 알아보는 - 분할 정복(순환 구조) vs 동적 계획법

def edit_distance(S,T,m,n): # 편집 거리 - 분할 정복 기법 (순환구조)
    if m == 0: return n # S가 공백이면, T의 모든 문자를 S에 삽입
    if n == 0: return m # T가 공백이면, S의 모든 문자들을 삭제

    if S[m-1] == T[n-1]:
        return edit_distance(S, T, m-1, n-1)
    
    return 1 + min(edit_distance(S,T,m,n-1), # 삽입
                   edit_distance(S,T,m-1,n), # 삭제
                   edit_distance(S,T,m-1,n-1)) # 대체

def edit_distance_mem(S, T, m, n, mem):  # 편집 거리 - 동적 계획법 (메모이제이션) : O(mn)
    if m == 0: return n
    if n == 0: return m

    if mem[m-1][n-1] == None:
        if S[m-1] == T[n-1]:
            mem[m-1][n-1] =  edit_distance_mem(S,T,m-1,n-1,mem)
        else:
            mem[m-1][n-1] = 1 + \
            min(edit_distance_mem(S, T, m, n-1,mem),
                edit_distance_mem(S, T, m-1, n,mem),
                edit_distance_mem(S, T, m-1, n-1,mem))
            
    return mem[m-1][n-1]

# 힙정렬

import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap,num)
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

print(heap_sort([6,8,3,9,10,1,2,4,7,5]))