# 1912943 고주희
# 1번을 해보세요!
def shortest_path_dijkstra(vtx, adj, start) :
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True

    for i in range(vsize):
        print("Step%2d: "%(i+1),dist)
        u = getMinVertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
    return path


# dist 배열에서 최소 가중치를 가진 정점을 찾는 함수
def getMinVertex(dist, selected) :
    minv = -1	
    mindist = INF
    for v in range(len(dist)) :					# 모든 정점들에 대해
        if not selected[v] and dist[v]<mindist :	# 선택 안 되었고  
            mindist = dist[v]						# 가중치가 작으면
            minv = v								# minv 갱신
    return minv					# 최소 가중치의 정점 반환


# 2번을 해보세요!
INF = 9999
vertex = [x for x in input().split()]
n = int(input())
weight = [[INF]*len(vertex) for _ in range(len(vertex))]
for i in range(len(vertex)):
    weight[i][i] = 0
for _ in range(n):
    a, b, c = input().split()
    weight[vertex.index(a)][vertex.index(b)] = int(c)
    weight[vertex.index(b)][vertex.index(a)] = int(c)


# 출력합니다!
print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)) :
    if end != start :
        print("[최단경로: %s->%s] %s" %
				(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start) :
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])
