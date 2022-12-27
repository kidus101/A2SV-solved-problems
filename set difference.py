# Enter your code here. Read input from STDIN. Print output to STDOUT

#Accepting Inputs

Eng = input()
English_List = list(map(int,input().split()))
Fren = input()
French_List = list(map(int,input().split()))

print(len(set(English_List).difference(set(French_List))))
