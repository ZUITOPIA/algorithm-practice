# 1912943 고주희
# 1번을 해보세요!
def sequential_search(A, key):
        for i in range(0, len(A)):
            if(key in A):
                if(key == A[i]):
                    return i
            else:
                return -1


# 2번을 해보세요!
A = list(map(int, input().split()))
key = int(input())

# 출력합니다!
print("%d찾기:" %(key), sequential_search(A, key))