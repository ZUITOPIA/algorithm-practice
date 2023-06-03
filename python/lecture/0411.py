# 삽입 정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
        printStep(A, i)

# 위상 정렬
mygraph = dict()

for i in range(int(input())):
    mygraph[chr(ord('A'+1))] = set()

for _ in range(int(input())):
    e1, e2 = input().split()[:2]
    mygraph[e1].add(e2) # mygraph[eq] | {e2}로 쓰는게 더 좋음

def topological_sort(graph):
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1

    vlist = []
    for v in graph:
        if inDeg[v] == 0:
            vlist.append(v)

    while vlist:
        v = vlist.pop()
        print(v, end=" ")

        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)

# 위상정렬 집합으로 입력 받기
mygraph = dict()
for i in range(int(input())):
    mygraph[chr(ord('A') + i)] = set()

for _ in range(int(input())):
    e1, e2 = input().split()[:2]
    mygraph[e1] |= {e2}

# 이진 탐색(순환구조)
def binary_search(A, key, low, high):
    if(low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1)
        else:
            return binary_search(A, key, mid + 1, high)
    return -1

# 이진 탐색(반복구조)
def binary_search_iter(A, key, low, high):
    while (low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 거듭 제곱 (억지기법)
def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result = result * x
    return result

# 거듭 제곱 (축소 정복 기법)
def power(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return power(x*x, n/2)
    else:
        return x * power(x*x, (n-1) // 2)
    
# 행렬의 거듭 제곱
n = int(input())
row = int(input())
x = [[int(m) for m in input().split()] for _ in range(row)]

def powerMat(x, n):
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multiMat(x,x), n // 2)
    else: 
        return multiMat(x, powerMat(multiMat(x,x), (n - 1) // 2))
    
# 정렬을 이용한 k 번째 작은 수 찾기
def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

# 축소 정복 기법을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if (pos + 1 == left + k):
        return A[pos]
    elif (pos + 1 > left + k):
        return quick_select(A, left, pos-1, k)
    else: 
        return quick_select(A, pos+1, right, k-(pos+1-left))
    
# 리스트 분할
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] <= pivot : low += 1 
        while high >= left and A[high] > pivot : high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] <= pivot : low += 1 
        while high >= left and A[high] > pivot : high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high


class TNode: # 이진트리를 위한 노드 클래스
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def calc_height(root) : # 이진트리의 높이
    if root is None:
        return 0
    
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1

# 입력
n = int(input())
binary_tree = [TNode(0,0,0) for _ in range(n)]

for i in range(n):
    data, left, right = [int(m) for m in input().split()[:3]]

    binary_tree[i].data = data
    binary_tree[i].left = binary_tree[left-1] if left > 0 else None
    binary_tree[i].right = binary_tree[right-1] if right > 0 else None

# 이진트리 전위 순회
def preorder(n) :
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

# 이진트리 중위 순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

# 이진트리 후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")

# 피보나치수열 (분할정복)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# 피보나치수열 (반복 구조)
def fib_iter(n):
    if (n<2) : return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

# 피보나치수열 (축소정복기법의 행렬거듭제곱 이용)
def fib_mat(n):
    if n < 2:
        return n
    mat = [[1,1], [1,0]]
    result = powerMat(mat, n)
    return result[0][1]

def powerMat(x, n) : # powerMat(x, n) 함수
	if n == 1 :
		return x
	elif (n % 2) == 0 :
		return powerMat(multMat(x,x), n // 2)
	else :
		return multMat(x, powerMat(multMat(x,x), (n - 1) // 2)) 


def multMat(M1, M2): # multMat(M1, M2) 함수
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result