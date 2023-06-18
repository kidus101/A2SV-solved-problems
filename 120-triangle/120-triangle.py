from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(row, col):
            if row == len(triangle):
                return 0

            lower_left = triangle[row][col] + dfs(row + 1, col)
            lower_right = triangle[row][col] + dfs(row + 1, col + 1)

            return min(lower_left, lower_right)

        return dfs(0, 0)
