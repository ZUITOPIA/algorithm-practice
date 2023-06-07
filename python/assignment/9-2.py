# 1912943 고주희
# 리스트로 주어지는 입력 S에서 합이 M인 모든 부분집합 찾기 함수
def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S, M, 0, [], sum(S))


# 1번을 해보세요!
def DFS_sum_of_subsets(S, M, level, sol, remaining):
    if sum(sol) == M:
        print(sol)
        return
    if sum(sol) > M:
        return
    
    for i in range(level, len(S)):
        sol.append(S[i])
        DFS_sum_of_subsets(S, M, i+1,sol, remaining-S[i])
        sol.pop()

# 2번을 해보세요!
nums = list(map(int, input().split()))
M = int(input())


# 출력합니다!
solution = all_sum_of_subsets(nums, M)
print("입력 집합 :", nums, "M=", M )