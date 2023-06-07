# 1912943 고주희

INF = 9999


# 1번을 해보세요!
def getMinVertex(dist, selected) :
    minv = -1	
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v]<mindist:
            mindist = dist[v]
            minv = v
    return minv


# 2번을 해보세요!
def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[0] = 0
    selected = [False] * vsize

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=":")
        print(dist)

        for v in range(vsize):
            if(adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]


# 3번을 해보세요!
vertex = input().split()
vsize = len(vertex)
n = int(input())
weight = [[None] * vsize for _ in range(vsize)]
for _ in range(n):
    i, j, w = input().split()
    i = ord(i) - ord('A')
    j = ord(j) - ord('A')
    w = int(w)
    weight[i][j] = w
    weight[j][i] = w

# 출력합니다!
print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)