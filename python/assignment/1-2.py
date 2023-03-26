# 1912943 고주희
# 1번을 해보세요!
a = int(input())
b = int(input())

# 2번을 해보세요!
def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
    
# 출력합니다!
print("%d, %d의 최대 공약수 =" % (a, b), gcd(a, b))
