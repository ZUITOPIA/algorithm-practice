# 호스풀 알고리즘 

# 1912943 고주희
NO_OF_CHARS = 128

# 1번을 해보세요!
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    return tbl


# 2번을 해보세요!
def search_horspool(T,P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else:
            i += t[ord(T[i])]
    
    return -1


# 3번을 해보세요!
text = input()
pattern = input()


# 출력합니다!
print("패턴의 위치 :", search_horspool(text, pattern))