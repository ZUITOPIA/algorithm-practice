# 카운팅 정렬

# 1912943 고주희
# 1번을 해보세요!
def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL 

    for i in A:
        count[i] += 1  

    for i in range(1, MAX_VAL):  
        count[i] += count[i-1]

    for i in range(len(A)):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i] 


# 2번을 해보세요!
data = [int(n) for n in input().split()]


# 출력합니다!
MAX_VAL = 10
print("Original  : ", data)
counting_sort(data)             # 카운팅 정렬
print("Counting  : ", data)