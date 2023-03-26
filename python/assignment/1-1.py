# 1912943 고주희
# 1번을 해보세요!
def find_max(a): 
    n = len(a)
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max
    

# 2번을 해보세요!
array = list(map(int,(input().split())))

# 출력합니다!
print(array, "최댓값=", find_max(array))