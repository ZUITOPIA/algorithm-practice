# 백트래킹

def all_permutations(data):
    bUsed = [False]*len(data)
    DFS_permutation(data, [], 0, bUsed)

def DFS_permutation(data,sol,level,bUsed):
    if level == len(data):
        print(sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            DFS_permutation(data, sol, level+1,bUsed)
            sol.pop()
            bUsed[i] = False
