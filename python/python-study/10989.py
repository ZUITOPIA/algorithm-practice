# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 이 문제의 포인트는 '메모리를 효율적으로 사용'하면서 정렬하는 것

import sys

input = sys.stdin.readline
N = int(input())
list = [0]*10001

for i in range(N):
    value = int(input())
    list[value-1] += 1

for i in range(10001):
    if list[i] != 0 :
        for j in range(list[i]):
            print(i+1)