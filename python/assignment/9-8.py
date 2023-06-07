# 1912943 고주희
import heapq

# 1번을 해보세요!
def job_assign_BFBnB(mat):
    N = len(mat)
    Q = []
    bound = calcBound(mat, [])
    heapq.heappush(Q, (bound+0, (0, bound, [])))

    while len(Q) > 0:
        total, (cost, bound, jobs) = heapq.heappop(Q)
        print("현재 노드: ", total, jobs)

        level = len(jobs)
        if level == N:
            return(total, jobs)

        for j in range(N):
            if j not in jobs:
                jbs = jobs+[j]
                cst = cost + mat[level][j]
                bnd = calcBound(mat, jbs)
                heapq.heappush(Q, (cst+bnd, (cst,bnd,jbs)))

# 2번을 해보세요!
def calcBound(mat, jobs):
    N = len(mat)
    J = len(jobs)
    bound = 0
    for i in range(J, N):
        min = 9999
        for j in range(N):
            if j not in jobs:
                if min > mat[i][j]:
                    min = mat[i][j]
        bound += min
    return bound


# 3번을 해보세요!
n = int(input())
Man2Job = [[int(m) for m in input().split()] for _ in range(n)]

# 출력합니다!
total, jobs = job_assign_BFBnB(Man2Job)
print("배정 결과: ", jobs)
print("전체 비용: ", total)