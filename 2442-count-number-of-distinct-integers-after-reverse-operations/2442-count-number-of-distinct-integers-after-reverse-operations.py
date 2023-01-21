class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        # Time:O(N) & SC:O(N)
        string_list = list()    
        tot_list = set()
        final_list = set()
#      Changing the int list to str list
        for num in nums:
            string_list.append(str(num))
#    creating a copy of string_list     
        for num in nums:
            tot_list.add(str(num))
# reversing the sting and adding to a set     
        for num in string_list:
            tot_list.add(num[::-1])
#   changing back to int to deal with "01 "== "10 " Problem    
        for num in tot_list:
            final_list.add(int(num))
        
        return len(final_list)
            
            
            
            
            
            
            
            
            
            