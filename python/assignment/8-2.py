# 1912943 고주희
# 1번을 해보세요!
def knapSack_fractional_greedy(obj, W): 
    obj.sort(key = lambda o: o[2]/o[1], reverse = True)

    totalValue = 0
    for o in obj:
        if W <= 0 :break
        if W - o[1] >= 0:
            W -= o[1]
            totalValue += o[2]
        else:
            fraction = W / o[1]
            totalValue += o[2] * fraction
            W = int(W - (o[1] * fraction))
    return totalValue

# 2번을 해보세요!
n = int(input())
obj = []
for _ in range(n):
    name, weight, value = input().split()
    obj.append((name, int(weight), int(value)))
W = int(input())


# 출력합니다!
print("W =", W, obj)
print(knapSack_fractional_greedy(obj,W)) 