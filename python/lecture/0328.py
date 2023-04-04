# 축소 정복 기법 (decrease and conquer) - 분할 정복 기법의 일종
# 예 : n! = n * (n-1)!

# 하향식 - 순환 (재귀 구조)
# 4! = 4 * 3!
#    = 4 * 3 * 2!
#    = 4 * 3 * 2 * 1!
#    = 4 * 3 * 2 * 1 = 24
def factorial_recur(n):
    if n == 1:
        return 1
    else:
        return (n * factorial_recur(n-1)) # 재귀

# 상향식 - 반복 구조
# 1! = 1
# 2! = 2 * 1! = 2 * 1 = 2
# 3! = 3 * 2! = 3 * 2 = 6
# 4! = 4 * 3! = 4 * 6 = 24
def factorial_iter(n):
    result = 1
    for k in range(1, n+1): # 반복문
        result = result * k
    return result

# 문제 축소 형태 : 고정 크기 축소(팩토리얼), 고정 비율 축소(이진 탐색, 거듭 제곱), 가변 크기 축소(유클리드 알고리즘)

