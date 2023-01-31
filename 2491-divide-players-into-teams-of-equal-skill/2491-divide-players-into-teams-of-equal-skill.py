class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0 
        right = len(skill) - 1
        
        storage = list()
        
        print(skill)
        # [1 , 2 , 3 , 4 , 5 , 6]
        
        while left < right:
            storage.append([skill[left] , skill[right]] )
            left += 1
            right -= 1
       
        sums = 0
        sum_list = list()
        for pair in storage:
            sums = sum(pair)
            sum_list.append(sums)
            
        total_product = 0
        
        if len(set(sum_list)) == 1:
            for pair in storage:
                total_product += prod(pair)
            return total_product 
    
        else:
            return -1
        