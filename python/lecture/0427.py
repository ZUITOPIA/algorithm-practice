# 기수 정렬
from queue import Queue

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue()) # BUCKETS 수 만큼 Queue 생성

    n = len(A)
    factor = 1
    for d in range(DIGITS): # 일의 자리부터 시작하여 (낮은자리부터 높은자리 순서로) 정렬
        for i in range(n):
            queues[(A[i] // factor) % 10].put(A[i]) # 모든 숫자에 대해 대응되는 BUCKET Queue에 삽입
        j = 0
        for b in range(BUCKETS): # BUCKET 안에 있는 숫자들을 첫번째 BUCKET부터 차례대로 뽑아서 리스트에 삽입
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10 # 자리수 마다 정렬할 수 있게 해주는 factor
        print("step", d+1, A)

# factor 이용
# 1234 // 10 = 123
# 1234 // 100 = 12
# 1234 // 1000 = 1


# 알고리즘 테스트(기수 정렬 테스트)
import random
BUCKETS = 10
DIGITS = 4
data = []
for i in range(10):
    data.append(random.randint(1, 9999))
radix_sort(data)
print("Radix(기수): ", data)

# 카운팅 정렬
def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL # 각 숫자가 몇 번씩 등장했는지 세기 위한 공간 생성 및 초기화

    for i in A:
        count[i] += 1 # 리스트 안의 각각의 숫자에 대응되는 빈도수를 증가
    
    for i in range(1, MAX_VAL): # 누적 빈도 배열로 변환
        count[i] += count[i-1]

    for i in range(len(A)):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i] 

# 호스풀 알고리즘의 시프트 테이블 만들기
NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    return tbl

# 호스풀 알고리즘
def search_horspool(T,P):
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

# 선형 조사법의 삽입 알고리즘
M = 13
table = [None]*M
def hashFn(key):
    return key % M

def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None):
        id = (id + 1 + M) % M
        count -= 1
    if count > 0:
        table[id] = key
    return 

# 선형 조사법의 탐색 알고리즘

def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] == key:
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

# 선형 조사법의 삭제 알고리즘
def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None : return
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

# 문자열 탐색키의 해시 함수 계산
def hashFn(key):
    sum = 0
    for c in key:
        sum = sum + ord(c)
    return sum % M