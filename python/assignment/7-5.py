# 배낭 채우기 알고리즘 (분할 정복 기법)

# 1912943 고주희
# 1번을 해보세요!
def knapSack_bf(W, wt, val, n): 
    if n == 0 or W == 0:
        return 0

    if(wt[n-1] > W):
        return knapSack_bf(W, wt, val, n-1)
    else:
        valWithout = knapSack_bf(W, wt, val, n-1)
        valWith = val[n-1] + knapSack_bf(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout)


# 2번을 해보세요!
n = int(input())
val = [int(i) for i in input().split()]
wt = [int(i) for i in input().split()]
W = int(input())


# 출력합니다!
print("최대 가치:", knapSack_bf(W, wt, val, n)) 