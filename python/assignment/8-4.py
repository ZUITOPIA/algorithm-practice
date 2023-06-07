# 1912943 고주희
# 서로소 집합 클래스
class disjointSets:
    def __init__(self, n):
        self.parent = [-1]*n    	# 각 노드는 모두 루트 노드
        self.set_size = n       	# 전체 집합의 개수	

    def find(self, id) :			# 정점 id가 속한 집합의 대표번호 탐색
        while (self.parent[id] >= 0) :	# 부모가 있으면(-1이 아닌 동안)
            id = self.parent[id]	# id를 부모 id로 갱신
        return id				# 최종 id 반환. 루트 노드의 id임

    def union(self, s1, s2) :		# 두 집합을 병합(s1을 s2에 병합시킴)
        self.parent[s1] = s2		# s1을 s2에 병합시킴
        self.set_size = self.set_size-1	# 집합의 개수가 줄어 듦


# 1번을 해보세요!
def MSTKruskal(V, adj):
    n = len(V)
    dsets = disjointSets(n)
    E = []
    for i in range(n-1):
        for j in range(i+1, n):
            if adj[i][j] != None:
                E.append((i, j, adj[i][j]))

    E.sort(key=lambda e:e[2])

    ecount = 0
    for i in range(len(E)):
        e = E[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        if uset != vset:
            dsets.union(uset, vset)
            print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
            ecount += 1
            if ecount == n-1:
                break


# 2번을 해보세요!
vertex = input().split()

n = int(input())
weight = [[None] * len(vertex) for _ in range(len(vertex))]
for _ in range(n):
    i, j, w = input().split()
    i = ord(i) - ord('A')
    j = ord(j) - ord('A')
    w = int(w)
    weight[i][j] = w
    weight[j][i] = w

# 출력합니다!
print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)