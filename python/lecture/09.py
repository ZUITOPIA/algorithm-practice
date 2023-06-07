# 백트래킹

### 순열 생성 알고리즘
def all_permutations(data):
    bUsed = [False]*len(data)
    DFS_permutation(data, [], 0, bUsed)

def DFS_permutation(data,sol,level,bUsed):
    if level == len(data):
        print(sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            DFS_permutation(data, sol, level+1,bUsed)
            sol.pop()
            bUsed[i] = False

### 합이 M인 부분집합 : O(2^n) - 백트래킹
def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S,M,0,[],sum(S))

def DFS_sum_of_subsets(S,M,level,sol,remaining):
    if sum(sol) == M:
        print(sol)
        return
    if sum(sol) > M:
        return
    
    for i in range(level, len(S)):
        sol.append(S[i])
        DFS_sum_of_subsets(S,M,i+1,sol,remaining-S[i])
        sol.pop()

### 미로탐색 - 백트래킹
def isSafeMaze(maze, x, y, mark):
    W,H = len(maze[0]),len(maze)
    if x >= 0 and x < W and y >= 0 and y < H:
        if maze[y][x]!=0 and mark[y][x] ==0:
            return True
        return False

def DFS_maze(maze,x,y,sol,mark):
    W, H = len(maze[0]), len(maze)

    if not isSafeMaze(maze,x,y,mark):
        return False
    
    mark[y][x] = 1
    sol[y][x] = 1
    if maze[y][x] == 2 :
        return True
    
    if DFS_maze(maze, x+1, y, sol, mark) == True: return True
    if DFS_maze(maze, x, y+1, sol, mark) == True: return True
    if DFS_maze(maze, x-1, y, sol, mark) == True: return True
    if DFS_maze(maze, x, y-1, sol, mark) == True: return True

    sol[y][x] = 0 # (x,y)는 이제 해의 일부가 아니기 때문에 sol에서 제거
    return False

def solve_maze(maze, x, y):
    W,H = len(maze[0]), len(maze)
    sol = [[0 for j in range(W)] for i in range(H)] # 미로 정답 (maze와 같은 크기)
    mark = [[0 for j in range(W)] for i in range(H)] # 미로 지나간 길 표시 (maze와 같은 크기)

    if DFS_maze(maze, x, y, sol, mark) == False:
        print("출구를 찾을 수 없음")
    else:
        for i in sol: print(i)


# N-Queen - 백트래킹
def isSafeQueen(board, x, y):
    N = len(board)

    for i in range(y): # 북쪽 방향 확인
        if board[i][x] == 1: return False
    for i, j in zip(range(y-1,-1,-1), range(x-1,-1,-1)): # 서북 방향
        if board[i][j] == 1: return False
    for i, j in zip(range(y-1,-1,-1), range(x+1, N)):# 동북 방향
        if board[i][j] == 1: return False
    return True

def printBoard(board): # 주어진 코드
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        printBoard(board)
        return
    
    for x in range(N):
        if isSafeQueen(board, x, y):
            board[y][x] = 1
            solve_N_Queen(board, y+1)
            board[y][x] = 0

# 그래프 색칠 - 백트래킹 
def isSafeGraph(g,v,c,color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True

def DFS_graph_coloring(graph,k,v,color):
    if v == len(graph):
        return True
    
    for c in range(1, k+1):
        if isSafeGraph(graph,v,c,color):
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0
    return False

def graphColoring(graph, k, states):
    color = [0]*len(graph)
    ret = DFS_graph_coloring(graph, k, 0, color)
    if ret:
        for i in range(len(graph)):
            print("%3s = "%states[i], color_name[color[i]]) # color_name 주어짐
    else:
        print("그래프를 색칠할 수 없음")

# 배낭채우기 - 분기 한정 기법
def printNode(knapsack, level, weight, profit, bound, maxProfit): # 주어진 코드
    print("%d %-16s :  %3.1fKg 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)"%
          (level, knapsack, weight, profit, bound, maxProfit))
    
def bound1(obj, W, level, weight, profit) :
    if weight > W:
        return 0
    
    pBound = profit
    for j in range(level+1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapSack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound) : 
    printNode(knapsack, level, weight, profit, bound, maxProfit)

    if (level == len(obj)) :
        return maxProfit

    if weight + obj[level][0] <= W :
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        if newProfit > maxProfit :
            maxProfit = newProfit

        newBound  = bound1(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit :
            knapsack.append(obj[level][2])
            maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight, 
									newProfit, maxProfit, newBound)  
            knapsack.pop()

    newWeight = weight
    newProfit = profit
    newBound  = bound1(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight,
									 newProfit, maxProfit, newBound) 

    return maxProfit

# 배낭채우기 - 분기 한정 기법 (개선된 한계가치 계산법) - 분할 가능한 경우
def printNode(knapsack, level, weight, profit, bound, maxProfit): # 주어진 코드
    print("%d %-16s :  %3.1fKg 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)"%
          (level, knapsack, weight, profit, bound, maxProfit))

def bound2(arr, W, level, weight, profit) :
    if weight > W:
        return 0
    
    pBound = profit
    tWeight = weight

    j = level + 1
    n = len(arr)
    while j < n  and (tWeight + obj[j][0] <= W):
        tWeight += arr[j][0]
        pBound += arr[j][1]
        j += 1

    if (j < n):
        pBound += (W-tWeight) * (arr[j][1]/arr[j][0])

    return pBound

def knapSack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound) : 
    printNode(knapsack, level, weight, profit, bound, maxProfit)

    if (level == len(obj)) :
        return maxProfit

    if weight + obj[level][0] <= W :
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        if newProfit > maxProfit :
            maxProfit = newProfit

        newBound  = bound2(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit :
            knapsack.append(obj[level][2])
            maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight, 
									newProfit, maxProfit, newBound)  
            knapsack.pop()

    newWeight = weight
    newProfit = profit
    newBound  = bound2(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight,
									 newProfit, maxProfit, newBound) 

    return maxProfit


# 일 배정 문제 - 최적 우선 분기 한정 
import heapq

def calcBound(mat, jobs):
    N = len(mat)
    J = len(jobs)
    bound = 0
    for i in range(J, N):
        min = 9999
        for j in range(N):
            if j not in jobs:
                if min > mat[i][j]:
                    min = mat[i][j]
        bound += min
    return bound

def job_assign_BFBnB(mat):
    N = len(mat)
    Q = []
    bound = calcBound(mat, [])
    heapq.heappush(Q, (bound+0, (0, bound, [])))

    while len(Q) > 0:
        total, (cost, bound, jobs) = heapq.heappop(Q)
        print("현재 노드: ", total, jobs)

        level = len(jobs)
        if level == N:
            return(total, jobs)

        for j in range(N):
            if j not in jobs:
                jbs = jobs+[j]
                cst = cost + mat[level][j]
                bnd = calcBound(mat, jbs)
                heapq.heappush(Q, (cst+bnd, (cst,bnd,jbs)))