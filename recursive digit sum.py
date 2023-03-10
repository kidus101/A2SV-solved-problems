
def superDigit(n, k):
    # string = int(str(n)*k)
    n=int(n)
    sum_ = 0
    
    while n:
        sum_ += n % 10
        n = n // 10
        
    n=sum_*k     
       
    def helper(sum_):
        
        if sum_ <= 9:
            return sum_
        
        n = 0
        
        while sum_:
            n += sum_ % 10
            sum_ = sum_ // 10
        
        return helper(n)
    
    return helper(n)
