# 1912943 고주희
# 필요한 모듈을 추가해 보세요!
import queue

# 1번을 해보세요!
def bfs(graph, start):
    visited = { start }
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end=" ")
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)


# 2번을 해보세요!
mygraph = dict()
n = int(input())
for i in range(n):
    e1, e2 = input().split()[:2]
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}


# 출력합니다!
print('BFS : ', end='')
bfs(mygraph, "A")
print()
