# 1912943 고주희
# 1번을 해보세요!
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)


# 2번을 해보세요!
mygraph = dict()
n = int(input())
for i in range(n):
    e1, e2 = input().split()[:2]
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}


# 출력합니다!
print('DFS : ', end='')
dfs(mygraph, "A", set() )
print()