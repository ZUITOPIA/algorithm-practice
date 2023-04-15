# 1912943 고주희
# 1번을 해보세요!
def binary_search_iter(A, key, low, high) :
    while(low <= high):
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key <= A[mid]:
            high = mid - 1
        else: 
            low = mid + 1 
    return -1


# 2번을 해보세요!
listA = [int(n) for n in input().split()]
key = int(input())


# 출력합니다!
print("입력 리스트 =", listA)
print("%d 탐색(반복) -->" %(key), binary_search_iter(listA, key, 0, len(listA)-1) )