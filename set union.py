# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
English_List = set(map(int,input().split()))
m = input()
French_List = set(map(int,input().split()))

print(len(English_List.union(French_List)))
