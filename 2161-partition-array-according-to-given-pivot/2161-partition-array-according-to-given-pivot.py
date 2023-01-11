class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan_list = list()
        greaterthan_list = list()
        pivot_list = list()
        final_list = list()
        
        for num in nums:
            if num < pivot :
                lessthan_list.append(num)
            elif num > pivot:
                greaterthan_list.append(num)
            else:
                pivot_list.append(num)    

           
        final_list =  lessthan_list + pivot_list +greaterthan_list
      
        return final_list

       # T:O(n) S:O(N)