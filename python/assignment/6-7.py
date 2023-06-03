# 문자열 탐색키의 해시 함수 계산

# 1912943 고주희
M = 13              # 테이블의 크기
table = [None]*M    # 테이블 만들기: None으로 초기화


# 1번을 해보세요!
def hashFn(key):
    sum = 0
    for c in key:
        sum = sum + ord(c)
    return sum % M


# 선형 조사법의 삽입 알고리즘
def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
    # while count>0 and (table[id] != None) :
        id = (id + 1 + M) % M
        count -= 1
    if count > 0 :
        table[id] = key	
    return

# 2번을 해보세요!
n = int(input())
for _ in range(n):
    lp_insert(input())


# 출력합니다!
print(table)