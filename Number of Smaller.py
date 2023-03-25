    n , m = map(int , input().split())
    array1 = list(map(int,input().split()))
    array2 = list(map(int,input().split()))
     
    ptr2 = 0
    output = []
    ptr1 = 0
     
    for ptr2 in range(m):
        
        while ptr1 < n and array1[ptr1] < array2[ptr2]:
            ptr1 += 1
        
        output.append(ptr1)
     
    print(*output)
