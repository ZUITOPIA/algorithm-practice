# 79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
# 문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

M, N = map(int, input().split())
dict = { "0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine" } # 주의!! dictionary일때의 index는 숫자가 아닌 문자
arr = []

for i in range(M, N+1):
    list = ''.join(dict[j] for j in str(i)) # 만약 "8"을 넣으면 dict["8"]인 "eight" 값이 list에 추가됨
    arr.append([i, list]) # 원소가 2개씩인 값을 arr 배열 안에 넣음, 예를 들면 [["8", "eight"], ["9", "nine"], ... ] 

arr.sort(key=lambda x:x[1]) # 만약 arr 배열이 [["8", "eight"], ["9", "nine"], ... ] 라면 원소들 중 1번째 원소를 기준으로 정렬

for i in range(len(arr)):
    if i % 10 == 0 and i != 0:
        print(sep="\n")
    print(arr[i][0], end=" ")