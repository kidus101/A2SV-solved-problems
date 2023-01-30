class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq_c = int(c ** 0.5)
        left = 0
        right = sq_c
        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False
