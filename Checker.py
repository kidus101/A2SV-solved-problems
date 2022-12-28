# Enter your code here. Read input from STDIN. Print output to STDOUT

# 
setA = set(map(int, input().split()))
n = int(input())
bool_list = list()

# Function that will check if the sets are super sets or not

def checker():
    sets = set(map(int, input().split()))
    
    if sets.issubset(setA):
        if len(setA) == len(sets):
            bool_list.append(0)
        else:
            bool_list.append(1)
    else:
        bool_list.append(0)    
 
        # Iterate through the input and run the function checker

for i in range(n):
    checker()
    
if all(bool_list) == 1:
    print(True) 
else:
    print(False)
    

     
            

