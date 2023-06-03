# Floyd의 최단 경로 탐색 알고리즘

# 1912943 고주희
import copy	

# 1번을 해보세요!
def shortest_path_floyd(vsize, W):
    D = copy.deepcopy(W)
    # 정점 k를 추가할 때마다 반드시 printD(D)를 호출하세요!

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if(D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)


# 현재의 최단거리 행렬 D를 화면에 출력하는 함수
def printD(D):
    vsize = len(D)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (D[i][j] == INF) : print(" INF ", end='')
            else : print("%4d "%D[i][j], end='')
        print("")


# 2번을 해보세요!
INF = 9999
vsize = int(input())
n = int(input())
weight = [[INF] * vsize for _ in range(vsize)]

for i in range(vsize):
    weight[i][i] = 0

for _ in range(n):
    i,j,w = [int(m) for m in input().split()[:3]]
    weight[i][j] = w
    weight[j][i] = w


# 출력합니다!
print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vsize, weight)
