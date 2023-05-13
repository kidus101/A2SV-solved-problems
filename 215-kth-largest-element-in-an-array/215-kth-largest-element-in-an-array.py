class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = [ -int(num) for num in nums]
        heapq.heapify(max_heap)
        
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return (-max_heap[0])
        # return str(-max_heap[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         nums=[-i for i in nums]
#         heapq.heapify(nums)
#         for i in range(k-1):
#             heapq.heappop(nums)
            
#         return -heapq.heappop(nums)
    
#     # Time:O(nlogn)
#     # Space:O(n)