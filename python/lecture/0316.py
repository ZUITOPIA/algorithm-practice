# 복잡도 분석
# 1. 입력의 크기
# 2. 알고리즘의 기본 연산
# 3. 입력 크기에 따른 증가 양상
# 4. 입력 내용의 속도 영향 여부

# 예 : 반복 알고리즘
# 1) 입력의 크기를 나타내는 파라미터를 결정
# 2) 기본 연산 찾기 (보통 반복 루프의 가장 안쪽에 있음) 
# 3) 연산의 횟수가 입력 크기에 의해서만 결정되는지 살펴보기, 만약 입력의 종류에 따라서도 다르다면 최선, 최악, 평균의 경우에 대해 독립적으로 복잡도를 분석해야 함
# 4) 기본 연산의 전체 실행 횟수를 구하는 복잡도 함수 T(n)을 구함
# 5) 알려진 공식 등을 이용해 T(n)을 풀고, 증가속도를 계산

# 예 : 순환 알고리즘
# 1) 입력의 크기를 나타내는 파라미터를 결정
# 2) 기본 연산 찾기
# 3) 연산의 횟수가 입력 크기에 의해서만 결정되는지 살펴보기
# 4) 기본 연산의 전체 실행 횟수를 구하기 위한 순환 관계식 T(n)을 구함 (이때, 초기 조건도 찾기)
# 5) 순환 관계식(점화식)을 풀거나 증가속도를 계산

# 순환 알고리즘 대표적 예 
# 1. 팩토리얼 계산 문제 (점근적 복잡도 O(n))
# 1-1 순환구조로 풀기
def factorial_1(n) :
    if n == 0:
        return 1
    else :
        return n * factorial_1(n-1)
# 1-2 반복구조로 풀기
def factorial_2(n):
    result = 1
    for k in range(n, 0, -1) : # k : n, n-1, ..., 2, 1
        result = result + k
    return result

# 2. 하노이 탑 문제
# Hanoi(N, start, tmp, to) = Hanoi(N-1, start, to, tmp) + move(N, start, to) + Hanoi(N-1, tmp, start, to)
def hanoi_tower(n, start, tmp, to) :
    if (n == 1) :
        print("원판 1: %s --> %s" % (start, to))
    else :
        hanoi_tower(n-1, start, to, tmp)
        print("원판 %d: %s --> %s" % (n, start, to))
        hanoi_tower(n - 1, tmp, start, to)