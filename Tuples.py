# Enter your code here. Read input from STDIN. Print output to STDOUT
# import hashlib

n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))
