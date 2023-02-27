t = int(input())

def catch_thief():
    n = int(input())
    array = list(map(int,input().split()))
    total_sum = 0
    flag =False
    # answer=0

    for i in range(n-1):

        if array[i] != 0:
            flag = True
        if flag and array[i] == 0:
            total_sum += 1
        elif flag and array[i] != 0:
            total_sum += array[i]

        # if answer and array[i] == 0:
        #     answer += 1
        # answer += array[i]

    print(total_sum)


for i in range(t):
    catch_thief()
