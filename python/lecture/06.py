# 공간으로 시간벌기 (동적계획법을 제외한, 나머지 방법들)

### 기수정렬
from queue import Queue

BUCKETS = 10 # 10진법으로 정렬
DIGITS = 4 # 최대 4 자릿수

def radix_sort(A):
    queues = []
    for i in range(BUCKETS): # 버킷의 수만큼 Queue 생성
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS): # 낮은 자리에서 높은 자리 순으로 반복하며 
        for i in range(n):
            queues[(A[i]//factor) % 10].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print("step", d+1, A)

### 카운팅 정렬
MAX_VAL = 10 # 0부터 9까지 10자리를 마련해놓을 것이므로 10으로 지정

def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL # 각 숫자를 세기 위한 공간 생성 및 초기화

    for i in A: # 리스트 안의 각각 숫자에 대응되는 빈도수를 증가 시키기
        count[i] += 1
    
    for i in range(1, MAX_VAL): # 누적 빈도 배열로 변환 ( 누적 빈도 사용하는 이유 : 그 값의 위치를 알려주기 때문 )
        count[i] += count[i-1]

    for i in range(len(A)): # 모든 원소에 대응되는 누적 빈도에 해당하는 위치에 키 값을 입력
        output[count[A[i]-1]] = A[i]
        count[A[i]] -= 1 # 같은 값이 여러번 나온 경우 같은 값이 있는 곳의 좌측에 넣어줌

    for i in range(len(A)):
        A[i] = output[i] # 임시 출력 리스트값을 입력 리스트 값으로 복사

### 호스풀 알고리즘 
# 복잡도 : 최악의 경우 O(mn) / 최선의 경우 O(n) 성능까지

NO_OF_CHARS = 128

text = input()
pattern = input()

def shift_table(pat): ### 호스풀 알고리즘의 시프트 테이블 만들기
    m = len(pat) # 패턴의 길이
    tb1 = [m]*NO_OF_CHARS # 시프트 테이블

    for i in range(m-1): # 패턴의 모든 문자에 대해서 그 알파벳이 패턴의 몇번째 문자인지
        tb1[ord(pat[i])] = m-1-i

    return tb1

def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else:
            i += t[ord(T[i])]
    return -1

print("패턴의 위치 :", search_horspool(text, pattern))

### 해싱 Hashing (공간으로 시간 벌기 전략의 가장 대표적인 예) - 선형 조사법의 삽입
M = 13 # 테이블의 크기
table = [None] * M # 테이블 만들기 : 모두 None으로 초기화

def hashFn(key):
    return key % M

def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None):
        id = (id + 1 + M) % M # 다음 위치로 이동
        count -= 1 # 검사할 남은 위치 수
    if count > 0:
        table[id] = key # 해당 슬롯에 항목 저장
    return

n = int(input())
for _ in range(n):
    lp_insert(int(input()))


### 해싱 Hashing (공간으로 시간 벌기 전략의 가장 대표적인 예) - 선형 조사법의 탐색 
def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return  None
        if table[id] == key: # 해시 함수가 가리킨 인덱스와 매칭
            return table[id] # 찾는 항목이 테이블에 있는 경우
        id = (id + 1 + M) % M # 값이 매칭되지 않으면 한칸씩 움직이면서 다음 위치 검사 반복
        count -= 1 # 모든 원소를 다 매칭하면(count == 0이면) 탐색 실패
    return None

table = [None if m == "None" else int(m) for m in input().split()]
key = int(input())

### 해싱 Hashing (공간으로 시간 벌기 전략의 가장 대표적인 예) - 선형 조사법의 삭제  
def lp_delete(key): 
    id = hashFn(key)
    count = M

    while count > 0:
        if table[id] == None: return
        if table[id] != -1 and table[id] == key:
            table[id] = -1 # 삭제할 값을 찾으면 삭제함 (값을 -1로 변경하기)
            return 
        id = (id + 1 + M) % M
        count -= 1

table = [None if m == "None" else int(m) for m in input().split()]
key = int(input())

### 해싱 - 삽입, 탐색, 삭제 공통되는 부분
count = M
while count > 0:
    id = (id + 1 + M) % M
    count -= 1

### 해시 함수 - 문자열 탐색키
def hashFn(key):
    sum = 0
    for c in key:
        sum = sum + ord(c)  # 각 문자의 아스키코드를 더해서 숫자를 만듦
    return sum % M 

n = int(input())
for _ in range(n):
    lp_insert(int(input()))