class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rows = len(grid)
        if rows == 0:
            return perimeter
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                
                if r == 0 or grid[r - 1][c] == 0:  # check upper
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # check lower
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # check left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # check right
                    perimeter += 1
                    
        return perimeter
