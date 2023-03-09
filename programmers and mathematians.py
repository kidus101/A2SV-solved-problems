    t = int(input())
     
    def team(t):
        p , m = map(int,input().split())
     
        min_ = min(p,m)
        average = (p + m) // 4
     
        if min_ >= average:
            print(average)
        else:
            print(min_)
     
    for i in range(t):
        team(i)
