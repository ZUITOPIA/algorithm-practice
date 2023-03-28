order = []

n = int(input())
selectArr = list(map(int, input().split()))

for i in range(n):
  order.insert(selectArr[i], i + 1)

print(*order[::-1])
