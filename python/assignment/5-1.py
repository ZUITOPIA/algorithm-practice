# 1912943 고주희
# 1번을 해보세요!
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)


# 2번을 해보세요!
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


# 3번을 해보세요!
data = [int(n) for n in input().split()]

# 출력합니다!
sorted = [0] * len(data)			# 길이가 len(data)인 임시 리스트를
print("Original  : ", data)			# 만들고 모든 항목을 0으로 초기화
merge_sort(data, 0, len(data)-1)	# 병합 정렬
print("MergeSort : ", data)


