# 1912943 고주희
# 1번을 해보세요!
def compute_square_C(n):
    sum = 0
    # 복잡도가 O(n^2)이 되도록 이중 for 문을 작성해보세요!
    for i in range(n):
        for j in range(n):
            sum = sum + 1
    return sum
    
# 2번을 해보세요!
n = int(input())

# 출력합니다!
print(compute_square_C(n))