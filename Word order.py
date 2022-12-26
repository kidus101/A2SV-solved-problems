# Enter your code here. Read input from STDIN. Print output to STDOUT
# TC:O(N) and SC:O(1)

from collections import Counter 

n = int(input())
newList = list()

for _ in range(n):
    newList.append(input())
    
countedList=Counter(newList)

print(len(countedList))
print(*countedList.values())


# go through the input array and check if there are equal words

# 1.cout << the Distnict words
# 2.cout << Number of occurence for each 

