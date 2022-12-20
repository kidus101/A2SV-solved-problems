from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countedNums = Counter(nums)
        
        for key,values in countedNums.items():
            if countedNums[key] == 1:
                return key