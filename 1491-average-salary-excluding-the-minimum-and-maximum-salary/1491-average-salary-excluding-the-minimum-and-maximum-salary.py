class Solution:
    def average(self, salary: List[int]) -> float:
        N = len(salary) 
        
        minimum = min(salary)
        maximum = max(salary)
        
        return (sum(salary) - minimum - maximum) / (N-2)
    
    # TC:O(1) and SC:O(1)