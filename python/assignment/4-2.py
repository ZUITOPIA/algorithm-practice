# 1912943 고주희
# 1번을 해보세요!
def topological_sort(graph):
    inDeq = {}
    for v in graph:
        inDeq[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeq[u] += 1
    vlist = []
    for v in graph:
        if inDeq[v] == 0:
            vlist.append(v)
    while vlist:
        v = vlist.pop()
        print(v, end=" ")
        for u in graph[v]:
            inDeq[u] -= 1
            if inDeq[u] == 0:
                vlist.append(u)
                
# 2번을 해보세요!
mygraph = dict()
for i in range(int(input())):
    mygraph[chr(ord('A') + i)] = set()
for _ in range(int(input())):
    e1, e2 = input().split()[:2]
    mygraph[e1] |= {e2}

# 출력합니다!
print('topological_sort: ')
topological_sort(mygraph)
print()