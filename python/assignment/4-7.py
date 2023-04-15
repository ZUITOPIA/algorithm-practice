# 1912943 고주희
# 1번을 해보세요!
def powerMat(x, n) :
    if n == 1:
        return x
    elif (n % 2) == 0:
        return powerMat(multMat(x,x), n // 2)
    else: 
        return multMat(x, powerMat(multMat(x,x), (n-1) // 2))

# 행렬을 곱하는 multMat(M1, M2) 함수에요!
def multMat(M1, M2):
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result

# 2번을 해보세요!
n = int(input())
row = int(input())
x = [[int(m) for m in input().split()] for _ in range(row)]

# 출력합니다!
result = powerMat(x, n)
print()
for row in result:
    for num in row:
        print(num, end=' ')
    print()