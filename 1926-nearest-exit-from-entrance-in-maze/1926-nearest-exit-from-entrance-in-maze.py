from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

        queue = deque([(entrance[0], entrance[1], 0)]) 
        maze[entrance[0]][entrance[1]] = '+' 

        while queue:
            curRow, curCol, level = queue.popleft()

            for dx, dy in directions:
                newRow, newCol = curRow + dx, curCol + dy

                if 0 <= newRow < rows and 0 <= newCol < cols and maze[newRow][newCol] == '.':
                    if (newRow == 0 or newRow == rows - 1 or newCol == 0 or newCol == cols - 1) and (newRow != entrance[0] or newCol != entrance[1]):
                        return level + 1

                    maze[newRow][newCol] = '+'  
                    queue.append((newRow, newCol, level + 1))

        return -1
