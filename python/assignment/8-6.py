# 1912943 고주희

import heapq
from queue import PriorityQueue

# 1번을 해보세요!
def make_heap_tree(freq, label):
    q = PriorityQueue()
    n = len(freq)
    h = []
    for i in range(n):
        q.put((freq[i], label[i]))

    for i in range(1, n):
        e1 = q.get()
        e2 = q.get()
        q.put((e1[0]+e2[0],e1[1]+e2[1]))
        print(e1, "+", e2)
    print(q.get())



# 2번을 해보세요!
label = input().split()
freq  = list(map(int, input().split()))


# 출력합니다!
make_heap_tree(freq, label)