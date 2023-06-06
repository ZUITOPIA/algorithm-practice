# 분할 정복 기법

### 병합 정렬 O(nlogn)

data = [int(n) for n in input().split()] # 입력 예시 : 5 3 8 4 9 1 6 2 7

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    k = left # 새롭게 만들어질 결과 배열의 맨 앞
    i = left # 쪼개진 리스트 중 앞 리스트의 맨 앞
    j = mid + 1 # 쪼개진 리스트 중 뒤 리스트의 맨 앞
    while i <= mid and j <= right:
            if A[i] <= A[j]:
                 sorted[k] = A[i]
                 i, k = i+1, k+1
            else:
                 sorted[k] = A[j]
                 j, k = j+1, k+1
    
    if i > mid:
         sorted[k:k+right-j+1] = A[j:right+1]
    else:
         sorted[k:k+mid-i+1] = A[i:mid+1]

### 퀵정렬

data = [int(n) for n in input().split()] # 입력 예시 : 5 3 8 4 9 1 6 2 7

def quick_sort(A, left, right):
     if left < right:
          mid = partition(A, left, right)
          quick_sort(A, left, mid-1)
          quick_sort(A, mid+1, right)

def partition(A, left, right):
     low = left + 1
     high = right
     pivot = A[left] # 리스트 A의 맨 앞 원소를 pivot으로 설정
     while(low <= high):
          while low <= right and A[low] <= pivot : low += 1
          while high >= left and A[high] >= pivot : high -= 1
          if low < high:
               A[low], A[high] = A[high], A[low]

     A[left], A[high] = A[high], A[left]
     return high

### 이진트리를 위한 노드 클래스
class TNode:
     def __init__(self, data, left, right):
          self.data = data
          self.left = left
          self.right = right

### 이진트리의 높이 문제

n = int(input())
binary_tree = [TNode(0,0,0) for _ in range(n)]

for i in range(n):
     data, left, right = [int(m) for m in input.split()[:3]]
     binary_tree[i].data = data
     binary_tree[i].left = binary_tree[left-1] if left > 0 else None
     binary_tree[i].right = binary_tree[right-1] if right > 0 else None
# 입력 예시 :
# 6
# 1 2 3
# 2 4 5
# 3 6 -1
# 4 -1 -1
# 5 -1 -1
# 6 -1 -1

def calc_height(root):
     if root is None:
          return 0
     hleft = calc_height(root.left)
     hright = calc_height(root.right)
     return max(hleft, hright) + 1

### 이진트리의 표준 순회 문제 (전위 순회 VLR) 
def preorder(n):
     if n is not None:
          print(n.data, end=" ")
          preorder(n.left)
          preorder(n.right)

### 이진트리의 표준 순회 문제 (중위 순회 LVR)
def inorder(n):
     if n is not None:
          inorder(n.left)
          print(n.data, end=" ")
          inorder(n.right)

### 이진트리의 표준 순회 문제 (후위 순회 LRV)
def postorder(n):
     if n is not None:
          postorder(n.left)
          postorder(n.right)
          print(n.data, end=" ")
 
### 피보나치수열 - [ 분할정복 : O(2^n) ] vs [ 반복구조 : O(n) ] vs [ 축소정복 : O(logn) ]

### 분할정복 피보나치수열 O(2^n) : 분할 정복으로 풀기에 좋지 않음 (불필요한 중복값을 많이 구하게 됨)
def fib(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     else :
          return fib(n-1) + fib(n-2)
     
### 반복구조 피보나치수열 O(n)
def fib_iter(n):
     if(n<2): return n
     last = 0
     current = 1
     for i in range(2, n+1):
          tmp = current
          current += last
          last = tmp
     return current

### 축소정복 피보나치수열 O(lonn)
def fib_mat(n):
     if n < 2:
          return n
     mat = [[1,1], [1,0]]
     result = powerMat(mat, n)
     return result[0][1]

def powerMat(x, n) :
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multMat(x,x), n // 2)
    else: 
        return multMat(x, powerMat(multMat(x,x), (n-1) // 2))

def multMat(M1, M2): # 행렬을 곱하는 multMat(M1, M2) 함수
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result