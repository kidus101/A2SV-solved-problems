class NumArray:
# # TC:O(N) & SC:O(1)
    def __init__(self, nums: List[int]):
        
        self.size = len(nums)
        
        self.prefix_sum = [0] * self.size

        self.prefix_sum[0] = nums[0]

        for k in range(1,self.size):
            self.prefix_sum[k] = self.prefix_sum[k-1] + nums[k]
        

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right]-self.prefix_sum[left-1]


        
        
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)