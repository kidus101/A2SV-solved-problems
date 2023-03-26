t = int(input())

def possible():
    n = int(input())
    array = list(map(int,input().split()))
    sorted(array)

    start = 0

    for i in range(n-1):
        if abs(array[i+1] - array[i]) <= 1:
            start += 1
    
    if start == n - 1:
        print("YES")
    else:
        print("NO")

for i in range(t):
    possible()
