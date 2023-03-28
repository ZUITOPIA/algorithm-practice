import sys # 시간초과 방지

n = int(sys.stdin.readline())
sticks = []
count = 1

for i in range(n):
  sticks.append(int(sys.stdin.readline()))

last = sticks[-1]

for i in range(len(sticks) - 1, -1, -1): # 맨 끝에서부터 역순으로 한 칸씩
  if sticks[i] > last:
    count += 1
    last = sticks[i]
    
print(count)
