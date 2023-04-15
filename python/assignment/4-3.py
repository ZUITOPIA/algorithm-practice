# 1912943 고주희
# 1번을 해보세요1
def binary_search(A, key, low, high) :
    if(low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search(A, key, low, mid-1)
        else:
            return binary_search(A, key, mid+1, high)
    return -1


# 2번을 해보세요!
listA = [int(n) for n in input().split()]
key = int(input())

# 출력합니다!
print("입력 리스트 =", listA)
print("%d 탐색(순환) -->" %(key), binary_search(listA, key, 0, len(listA)-1) )