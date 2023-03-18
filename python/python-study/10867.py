# N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.

# N = int(input())
# arr = []
#
# for i in range(N):
#     arr.append(int(input()))
#
# result = sorted(set(arr))
# print(result)

N = int(input())
arr = list(sorted(set(map(int, input().split()))))

for i in arr:
    print(i, end = ' ')