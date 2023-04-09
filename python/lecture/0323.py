# 선택 정렬 : O(n^2)
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (A[j] < A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1)

# 선택 정렬 알고리즘 테스트
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
selection_sort(data)
print("Selection: ", data)

# 순차 탐색 : 최선 O(1) / 최악 O(n) / 평균 O(n)
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
    
# 억지 기법
# 1. 문자열 매칭 : 최선 O(m) / 최악 O(mn)
# n : 리스트 길이 , m : 찾고자하는 패턴의 길이
def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]:
            j = j + 1
        if j == m:
            return i
    return -1

# 2. 최근접 점의 쌍의 거리 : O(n^2)
import math
import sys
INF = sys.maxsize

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist

print("최근점 거리:", closest_pair(p))

# 완전 탐색
# -> 상태공간트리의 모든 단말 노드를 검사하여 길이가 최소인 것을 선택하는 전략
# 예 ) 틱택토 게임, 
# 외판원 문제(TSP 완전탐색) - 그래프가 n개의 정점을 갖는 완전 그래프라면 모든 해밀토니안 사이클은 (n-1)!개 : O(n!)
# 배낭 채우기 문제 : O(2^n)
# 일 배정 문제 : O(n!)

# 그래프의 순회 BFS / DFS
# n (정점의 수), e (간선의 수)
# 인접 리스트 표현 : O(n+e)
# 인접 행렬 표현 : O(n^2)

# BFS
import queue
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

# DFS
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)