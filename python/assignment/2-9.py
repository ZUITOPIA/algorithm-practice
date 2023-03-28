# 1912943 고주희
# 1번을 해보세요!
n = int(input())

# 2번을 해보세요!
def hanoi_tower(n, fr, tmp, to):
    if(n == 1):
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n-1,fr,to,tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n-1,tmp,fr,to)
    

# 출력합니다!
hanoi_tower(n, "A","B","C")