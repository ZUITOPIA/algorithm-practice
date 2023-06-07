# 1912943 고주희
# 1번을 해보세요!
def min_coins_greedy( coins, V ): 
    count = []
    for i in range(len(coins)):
        cnt = V // coins[i]
        count.append(cnt)
        V -= cnt * coins[i]
    return count


# 2번을 해보세요!
coins = [int(n) for n in input().split()]
V = int(input())


# 출력합니다!
print("잔돈 액수 = ", V)
print("동전 종류 = ", coins)
print("동전 개수 = ", min_coins_greedy(coins, V ))

