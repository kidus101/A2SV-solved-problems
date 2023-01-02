from collections import defaultdict

n , m = list(map(int , input().split()))

dictionary = defaultdict(list)
list1 = list()

for i in range(1 , n + 1):
    dictionary[input()].append(i)

for j in range(m):
    list1.append(input())

for k in list1:
    if k in dictionary.keys():
        print(*dictionary[k])
    else:
        print(-1)
