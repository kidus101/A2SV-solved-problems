class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        # Row And Column 
        m = len(grid)
        n = len(grid[0])

        diff = [[0 for i in range(n)] for j in range(m)]


        rows = [0]* m
        colm = [0]* n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    colm[j] += 1
                # else
        for row in range(m):
            for col in range(n):
                diff[row][col] = rows[row] + colm[col] -((m - rows[row]) + (n -colm[col]))

        return diff