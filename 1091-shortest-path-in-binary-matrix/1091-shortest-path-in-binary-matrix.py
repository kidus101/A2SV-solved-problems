class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if 1 in (grid[0][0], grid[-1][-1]):
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        q = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        
        while q:
            x, y, distance = q.popleft()
            if (x, y) == (COLS - 1, ROWS - 1):
                return distance
            
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                
                if 0 <= newX < COLS and 0 <= newY < ROWS and (newX, newY) not in visited and grid[newX][newY] == 0:
                    q.append((newX, newY, distance + 1))
                    visited.add((newX, newY))
                    
        return -1