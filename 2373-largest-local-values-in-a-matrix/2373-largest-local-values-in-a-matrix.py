class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid[0])
        maxLocal = [[0 for _ in range(n-2)] for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        maxLocal[i][j] = max(maxLocal[i][j] , grid[ii][jj])
        
        return maxLocal
        
        
        
    #output is a 3*3 Matrix
    # Finding the largest element in a 3*3 Matrix in grid
    