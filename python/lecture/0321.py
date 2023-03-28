# 순차 탐색
A = [int(n) for n in input().split()]
key = ... # 놓쳤다!
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

# is / ==
# is는 '같은 객체인지'를 판단
A = [1,2,3]
B = [1,2,3]
C = A

A is B # false, 같은 객체가 아님 (서로 다른 메모리에 있기 때문에 둘이 다르다고 판단)
A is C # true, 값을 복사한 것이 아니라 A의 주소값을 복사하였기 때문에
A == B # true
A == C # true

D = "123"
E = "123"
F = input() # "123" 넣었을때

D is E # true, 문자열상수 취급 -> 같은 주소값을 가리키도록 만들기 떼문에
D is F # false, 새로 넣어줄 때는 다른 메모리에 할당되기 때문에
D == E # true
D == F # true
# 문자열은 배열이 아니기 때문에 D[1] = "2" 이런 일은 있을 수 없음 !!!


# 리스트의 중복 항목 탐색 문제
A = [int(n) for n in input().split()]
def unique_elements(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i] == A[j]:
                return False
    return True

        

# 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# 팩토리얼 함수를 for 문으로 바꾸기
def factorial_1(n):
    result = 1
    for k in range(n, 0, -1):
        result = result * k
    return result

# 자연수의 이진수 변환에서 총 비트수 계산
def binary(n):
    count = 1
    while n > 1:
        count = count +1
        n = n // 2
    return count

# 자연수의 이진수 변환에서 총 비트수 계산(순환)
def binary_digits(n):
    if n <= 1: 
        return 1
    else:
        return 1 + binary_digits(n // 2)