    n , m = map(int,input().split())
     
    array1 = list(map(int,input().split()))
    array2 = list(map(int,input().split()))
    output = list()
     
    ptr1 = 0
    ptr2 = 0
     
    while ptr1 < n and ptr2 < m:
        if array1[ptr1] < array2[ptr2]:
            output.append(array1[ptr1])
            ptr1 += 1
        else:
            output.append(array2[ptr2])
            ptr2 += 1
     
    output.extend(array1[ptr1:])
    output.extend(array2[ptr2:])
     
    print(*output)
