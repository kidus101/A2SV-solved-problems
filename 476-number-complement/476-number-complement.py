class Solution:
    def findComplement(self, num: int) -> int:
        binary = (bin(num)[2:])
        
        ones = int("1"*len(binary),2)
        
        complement = (num ^ ones)
        
        return complement
        