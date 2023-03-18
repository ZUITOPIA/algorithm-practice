# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input())
list = []

for i in range(N):
    list.append(int(input()))
list.sort()
for i in range(len(list)):
    print(list[i])
