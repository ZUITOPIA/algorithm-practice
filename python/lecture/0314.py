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