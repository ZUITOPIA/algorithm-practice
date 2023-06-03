# 피보나치 수열 (축소정복기법의 행렬의 거듭제곱 이용)

# 1912943 고주희
# 1번을 해보세요!
def fib_mat(n):
    if n < 2:
        return n
    mat = [[1,1], [1,0]]
    result = powerMat(mat, n)
    return result[0][1]


# powerMat(x, n) 함수
def powerMat(x, n) :
	if n == 1 :
		return x
	elif (n % 2) == 0 :
		return powerMat(multMat(x,x), n // 2)
	else :
		return multMat(x, powerMat(multMat(x,x), (n - 1) // 2)) 


# multMat(M1, M2) 함수
def multMat(M1, M2):
    result = [[0 for _ in range(len(M2[0]))] for __ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                result[i][j] += M1[i][k] * M2[k][j]
    return result


# 2번을 해보세요!
n = int(input())


# 출력합니다!
print(fib_mat(n))