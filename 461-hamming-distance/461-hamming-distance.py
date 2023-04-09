class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = str(bin(x ^ y)[2:])
        count = 0
        
        for num in xor:
            if num == "1":
                count += 1
        
        return count