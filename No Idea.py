# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
happiness = 0
array = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))


for num in array:
    if num in setA:
        happiness += 1
    if num in setB:
        happiness -= 1
        
print(happiness)
