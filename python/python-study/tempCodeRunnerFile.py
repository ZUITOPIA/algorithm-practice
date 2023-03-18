N = int(input())
array = sorted(list(set(map(int, input().split()))))

for i in array:
    print(' '.join(array))