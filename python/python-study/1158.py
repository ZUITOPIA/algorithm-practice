import sys

n, k = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n + 1)]
result = []
count = 0

for i in range(n):
  count += k - 1 # 몇 번째 숫자를 빼는 지 맞춰주기 위함
  if count >= len(arr):
    count = count % len(arr)
  result.append(str(arr.pop(count)))

print("<", ", ".join(result), ">", sep='')
