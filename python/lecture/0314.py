# range(start, end, step) => start 이상, end 미만, step 간격으로

# 최댓값을 찾는 알고리즘 1
def find_max(A):
    max = A[0]
    for i in range(len(A)): # range(1, len(A))가 더 좋음!
        if A[i] > max:
            max = A[i]
        return max
    
# 최댓값을 찾는 알고리즘 2    
def find_max2(A): # A가 리스트일 때
    max = A[0]
    # max = sys.minsize 
    # sys 사용하려면 import sys 해야함
    for a in A:
        if a > max:
            max = A
        return max
    
# 공백으로 구분되어 입력되는 숫자들을 받아서 array에 저장하기
array = [int(n) for n in input().split()]

# str.split()
"1 2 3".split() # ['1','2','3']
"1 2 3".split(" ") # ['1','2','3']
"1,2,3".split() # ['1,2,3']
"1,2,3".split(",") # ['1','2','3']
"1,2,,3".split(",") # ['1','2','','3']
"1,2,,3".split(",,") # ['1,2','3']
"   1  2  3   ".split(" ") # ['','','','1','','2','','3','','','']
"   1  2  3   ".split() # ['1','2','3']

# 최대공약수 문제 1
# 1. a와 b에 저장될 자연수가 한 줄에 하나씩 주어집니다. 이때 a는 b보다 작지 않습니다. 값을 받아서 a와 b에 각각 저장해보세요.
# 입력 예시
# 60
# 28

a = int(input())
b = int(input())

print("%d,%d의 최대공약수 = " % (a,b), gcd(a,b))

# 최대공약수 문제 2
# 2. 자연수 a와 b의 최대공약수를 return 하는 함수 gcd(a,b)를 완성해보세요.
# 출력 예시
# 60, 28의 최대공약수 = 4
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# 리스트 : ArrayList / LinkedList
# LinkedList : singly, circular, doubly, circular doubly
# structure { int value; Node* ptr; } Node
# 맨 첫번째 원소를 Head로 설정 (맨 마지막 원소를 tail로 설정하는 것은 optional)

list = ['a','b','c']
value = list.pop() # ['a','b'] 맨 마지막 원소 삭제됨

# 주의, 파이썬은 ArrayList이기때문에 Queue구조는 적합하지 않음!
# 원소의 갯수가 고정적일때는 ArrayList가 좋음

# LinkedList vs ArrayList
#       LinkedList : list 길이가 4인데 6개의 원소를 집어 넣는다면 ?
#           - 계속 노드를 하나씩 추가하면서 원소갯수에 맞게 늘려감
#       ArrayList : list 길이가 4인데 6개의 원소를 집어 넣는다면 ? doubling 함
#           - 기존 길이 4의 list를 길이 8의 list로 만듦 (allocation -> memcopy -> pree)
