class Solution: 
    def countAsterisks(self, s: str) -> int:
        res, flag = 0, True
        for i in s:
            if i == '|':
                flag = not flag
            if flag and i == '*':
                res += 1
        return res
        