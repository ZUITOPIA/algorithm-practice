for _ in range(int(input())):
  n = int(input())
  count = 0
  while n > 0:
    if n % 2 == 1:
      print(count, end=" ")
    n = n // 2
    count += 1