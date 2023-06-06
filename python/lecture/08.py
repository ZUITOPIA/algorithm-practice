# 탐욕적 기법

### 거스름돈 동전 최소화 : O(m) 
def min_coins_greedy(coins, V):
    count = []
    for i in range(len(coins)):
        cnt = V // coins[i]
        count.append(cnt)
        V -= cnt*coins[i]
    return count

# 분할 가능한 배낭 채우기 : O(n log n)
def knapSack_fractional_greedy(obj, W):
    obj.sort(key=lambda o:o[2]/o[1], reverse=True)

    totalValue = 0
    for o in obj:
        if W <= 0 : break
        if W - o[1] >= 0:
            W -= o[1]
            totalValue += o[2]
        else:
            fraction = W / o[1]
            totalValue += o[2] * fraction
            W = int(W - (o[1]*fraction))

    return totalValue

### 신장트리 : 그래프 내의 모든 정점을 포함하는 트리
### 최소비용 신장트리 (MST) : 간선들의 비용을 최소화하는 신장트리
def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj): # 최소비용 신장트리 - Prim 알고리즘
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


### 최소비용 신장트리 - kruskal 알고리즘
class disjoinSets:
    def __init__(self, n):
        self.parent = [-1]*n
        self.set_size = n

    def find(self, id):
        while(self.parent[id] >= 0):
            id = self.parent[id]
        return id
    
    def union(self,s1,s2):
        self.parent[s1] = s2
        self.set_size = self.set_size - 1


def MSTKruskal(V, adj): # 최소비용 신장트리 - Kruskal 알고리즘 : O(n^2 + eloge)
    # 순환 사이클을 만들지 않으면서도 가장 최소의 가중치들을 순서대로 선택하는 것
    n = len(V)
    dsets = disjoinSets(n)
    E = []
    for i in range(n-1):
        for j in range(i+1, n):
            if adj[i][j] != None:
                E.append(i, j, adj[i][j])
    E.sort(key=lambda e:e[2])

    ecount = 0
    for i in range(len(E)):
        e = E[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        if uset != vset:
            dsets.union(uset, vset)
            print("간선 추가 : (%s, %s, $d)" % (V[e[0]], V[e[1]],e[2]))
            ecount += 1
            if ecount == n-1:
                break
    # 만약 인접행렬이 아닌 인접리스트로 표현했다면 ? O(eloge)

def shortest_path_dijkstra(vtx,adj,start): # 다익스트라 알고리즘 : O(n^2)
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True

    for i in range(vsize):
        print("Step%2d: "%(i+1), dist)
        u = getMinVertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
    return path

### 허프만 트리
from queue import PriorityQueue 

def make_heap_tree(freq, label):
    q = PriorityQueue()
    n = len(freq)
    h = []
    for i in range(n):
        e1 = q.get()
        e2 = q.get()
        q.put((e1[0] + e2[0], e1[1] + e2[1]))
        print(e1, "+", e2)
    print(q.get())