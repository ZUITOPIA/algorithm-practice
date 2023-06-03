# 병합정렬 (call by value 작동)
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge_sort(A, left, mid, right)


A[left:(r+1)] = sorted[left:(r+1)] # call by value

A = sorted # call by ref
A[:] = sorted[:]
A = list(sorted) # 정석

# call by value
import copy
A = copy.deepcopy(sorted)

# 정렬된 두 리스트의 정렬
def merge(A, left, mid, right):
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right :
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i,k = i+1, k+1
        else:
            sorted[k] = A[j]
            j,k = j+1, k+1

    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    
    A[left:right+1] = sorted[left:right+1]



# 퀵정렬
def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

# 이진트리
# 모든 노드에 빈 값을 정의해두고 이후 갱신하는 방법으로

# 전위
# 중위
# 후위

# 피보나치수열(분할정복)
# 피보나치수열(반복구조)
# 피보나치수열(축소정복기법의 행렬거듭제곱)