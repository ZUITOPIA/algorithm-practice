# 1912943 고주희
# 1번을 해보세요!
def isSafe(g, v, c, color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True


# 2번을 해보세요!
def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True

    for c in range(1, k+1):
        if isSafe(graph, v, c, color):
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0
    return False


# 그래프 색칠 주 함수
def graphColoring(graph, k, states): 
    color = [0] * len(graph)       # 정점의 색 배정 리스트: 초기 0
    ret = DFS_graph_coloring(graph, k, 0, color)  # 0번 정점부터 처리
    if ret : 
        for i in range(len(graph)) :
            print("%3s = "%states[i], color_name[color[i]])
    else :
        print("그래프를 색칠할 수 없음!")


# 3번을 해보세요!
k = int(input())


# 출력합니다!
states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]
g = [ [0, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 0, 0, 1, 1, 0],
      [1, 1, 1, 0, 1, 1],
      [0, 0, 1, 1, 0, 1],
      [0, 0, 0, 1, 1, 0],]
print("색상 %d개:" %(k))
graphColoring(g, k, states) 
