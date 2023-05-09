class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        negativePiles = [-p for p in piles]
        
        total = sum(piles)
        heapq.heapify(negativePiles)
        
        for _ in range(k):
            max_ = heapq.heappop(negativePiles)
            
            decrement = math.floor(-max_ / 2)
            total -= decrement
            
            heapq.heappush(negativePiles, max_ + decrement)
            
        return total