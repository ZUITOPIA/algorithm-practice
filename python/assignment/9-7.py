# 1912943 고주희
# 노드를 탐색하는 순서와 각 노드에서 계산된 값들을 출력하는 함수
def printNode(knapsack, level, weight, profit, bound, maxProfit):
    print("%d %-16s :  %3.1fKg 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)"%
          (level, knapsack, weight, profit, bound, maxProfit))

# 분기 한정을 이용한 0-1 배낭 채우기 함수 
def knapSack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound) : 
    printNode(knapsack, level, weight, profit, bound, maxProfit)

    if (level == len(obj)) :
        return maxProfit

    if weight + obj[level][0] <= W :
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        if newProfit > maxProfit :
            maxProfit = newProfit

        newBound  = bound2(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit :
            knapsack.append(obj[level][2])
            maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight, 
									newProfit, maxProfit, newBound)  
            knapsack.pop()

    newWeight = weight
    newProfit = profit
    newBound  = bound2(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj, knapsack, W, level+1, newWeight,
									 newProfit, maxProfit, newBound) 

    return maxProfit


# 1번을 해보세요!
def bound2(arr, W, level, weight, profit) :
    if weight > W:
        return 0
    
    pBound = profit
    tWeight = weight

    j = level + 1
    n = len(arr)
    while j < n  and (tWeight + obj[j][0] <= W):
        tWeight += arr[j][0]
        pBound += arr[j][1]
        j += 1

    if (j < n):
        pBound += (W-tWeight) * (arr[j][1]/arr[j][0])

    return pBound


# 2번을 해보세요!
n = int(input())

obj = []
for _ in range(n):
    weight, value, name = input().split()
    obj.append((float(weight), float(value), name))

W = int(input())


# 출력합니다!
obj.sort(key= lambda e : e[1]/e[0], reverse=True)
print(obj)
print("0-1배낭문제(분기 한정): ", knapSack_bnb(obj, [], W, 0,0,0,0, 0) )
