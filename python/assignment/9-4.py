# 1912943 고주희
# 1번을 해보세요!
def isSafe(board, x, y):
    N = len(board)

    for i in range(y):
        if board[i][x] == 1: return False
    for i, j in zip(range(y-1, -1, -1), range(x-1,-1,-1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] == 1: return False
    return True

# 2번을 해보세요!
def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        printBoard(board)
        return
    
    for x in range(N):
        if isSafe(board, x, y):
            board[y][x] = 1
            solve_N_Queen(board, y+1)
            board[y][x] = 0

# 출력 함수
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# 3번을 해보세요!
N = int(input())

# 출력합니다!
board = [[0 for i in range(N)] for j in range(N)]
solve_N_Queen(board, 0)