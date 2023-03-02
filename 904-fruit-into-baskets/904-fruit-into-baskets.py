class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # TC:O(N) & SC:O(N)
        
        basket_dict = defaultdict(int)
        
        max_count = 0
        left = 0
        right = 0
        
        for right in range(len(fruits)):
            
            basket_dict[fruits[right]] += 1
            
            while len(basket_dict) > 2:
                basket_dict[fruits[left]] -= 1
                
                if basket_dict[fruits[left]] == 0:
                    basket_dict.pop(fruits[left])
                    
                left += 1

            max_count = max(max_count , right-left+1)
            
        return max_count
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         start, end = 0 , 0
#         max_len =0
#         d={}
        
#         while end < len(tree):
#             d[tree[end]] = end
            
#             if len(d) >= 3:
#                 min_val = min(d.values())
#                 del d[tree[min_val]]
#                 start = min_val +1
#             max_len = max(max_len, end - start + 1)
#             end += 1
#         return max_len
    
    #Time complexity :O(n)
    #Space Complexity: O(1)