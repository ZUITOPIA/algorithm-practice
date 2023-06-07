# 1912943 고주희
# 1번을 해보세요!
def all_permutations(data):
    bUsed = [False] * len(data)
    DFS_permutation (data, [], 0, bUsed)


# 2번을 해보세요!
def DFS_permutation (data, sol, level, bUsed):
    if level == len(data):
        print(sol)
        return
    
    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            DFS_permutation(data, sol, level+1, bUsed)
            sol.pop()
            bUsed[i] = False

# 3번을 해보세요!
data = input().split()


# 출력합니다!
all_permutations(data)
