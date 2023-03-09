class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        answer = []
        candidate = []
        
        def combination(index,k,candidate):
            if k == 0:
                answer.append(candidate.copy())
                return
            
            for idx in range(index , n ):
                
                candidate.append(idx+1)
                combination(idx+1 ,k-1,candidate)
                candidate.pop()
        
        combination(0,k,candidate)
        
        return answer
                