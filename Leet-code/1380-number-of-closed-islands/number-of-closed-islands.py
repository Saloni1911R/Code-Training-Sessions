class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds, it's not closed (though boundary clearing handles edges)
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # If it's water (1), return True
            if grid[r][c] == 1:
                return True
            
            # Mark current cell as visited (turn land '0' to water '1')
            grid[r][c] = 1
            
            # Explore all 4 directions
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            
            # A component is closed only if all 4 directions return True
            return left and right and up and down

        # Step 1: Eliminate all lands connected to the grid boundaries
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    self.fill_boundary(grid, r, c)

        # Step 2: Count remaining closed islands
        closed_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_islands += 1
                    self.fill_boundary(grid, r, c)
                    
        return closed_islands

    def fill_boundary(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])
        stack = [(r, c)]
        grid[r][c] = 1
        while stack:
            curr_r, curr_c = stack.pop()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    stack.append((nr, nc))
