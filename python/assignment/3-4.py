# 1912943 고주희
# 필요한 모듈을 추가해 보세요!
import math

# 1번을 해보세요!
def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# 2번을 해보세요!

n = int(input())
p = []
for i in range(n):
    pt = tuple([int(n) for n in input().split()])
    p.append(pt)

# 출력합니다!
print("최근접 거리:", closest_pair(p))