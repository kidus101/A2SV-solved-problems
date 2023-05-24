class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        
        a = []
        b  = []
        
        n = len(costs)
        middle = n//2
        
        
        for i in range(middle):
            a.append(costs[i][0])
            
        for i in range(middle,n):
            b.append(costs[i][1])
        
        return sum(a) + sum(b)