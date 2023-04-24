class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [False] * (right + 1)
        
        last_prime = -1
        result = [-1, -1]
        
        for prime in range(2, right+1):
            
            if not sieve[prime]:
                
                for p2 in range(prime*2, right+1, prime):
                    sieve[p2] = True
                    
                if left <= prime <= right:
                    
                    if last_prime == -1:
                        last_prime = prime
                        
                    elif result == [-1, -1]:
                        result = [last_prime, prime]
                        
                    elif prime - last_prime < result[1] - result[0]:
                        result = [last_prime, prime]
                        
                    last_prime = prime
                    
        return result
        