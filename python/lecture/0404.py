# 공백으로 나누어진 정수 리스트
# 10 20 30 40 50 -> [10, 20, 30, 40, 50]
# A = [int(n) for n in input().split()]

# 공백으로 나누어진 정수 튜플
# 10 20 30 40 50 -> (10, 20, 30, 40, 50)
# B = tuple(int(n) for n in input().split())

# 공백으로 나누어진 2개의 정수 튜플
# 10 20 30 40 50 -> (10, 20)
# C = tuple(int(n) for n in input().split()[:2])          // 앞에서 2개

# 공백으로 나누어진 2개의 정수 튜플 3쌍 (리스트)
# 10 20 
# 30 40
# 50 60
# -> [(10,20),(30,40),(50,60)]
# D = [tuple(int(n) for n in input().split()[:2]) for i in range(3)]  

# for i in range(3) == for _ in range(3)     // 불필요한 i 선언 없이

# 공백으로 나누어진 2개의 정수 튜플 n쌍 (리스트)
# E = [tuple(int(n) for n in input().split()[:2]) for _ in range(n)]  

# set vs list
# set은 순서X, 중복X

# 파이썬 집합 set
# | 합집합
# & 교집합
# - 차집합

# 파이썬 딕셔너리 dictionary
# {key1: value1, key2: value2, key3: value3, ...}
# 예시 ) mydict = {"a" : 1, "b" : 2, "c" :3}
# mydict["a"]        // 1
# mydict["b"]        // 2
# mydict["c"]        // 3
# mydict["d"]        // error
# "a" in mydict      // True
# "d" in mydict      // False
# mydict.get("a")    // 1
# mydict.get("d")    // None
# mydict.get("d") == None     // True
# mydict.setdefault("a")        // 1
# mydict.setdefault("a", 4)         // 1  (key가 있으면 value 반환)
# mydict.setdefault("d")        // None
# mydict.setdefault("d", 4)         // 4  (key가 없으면 두번째 value 반환)

# 파이썬에서 { } 는 empty dictionary 임. empty set 아님!!
# empty set 은 set()으로 표현해야 함