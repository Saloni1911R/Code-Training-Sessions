class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Memoization cache for structural reflections: (r, c, direction) -> (next_r, next_c, next_dir)
        # direction: 0 for Right, 1 for Down
        memo = {}
        
        def resolve_step(r, c, direction):
            state = (r, c, direction)
            if state in memo:
                return memo[state]
            
            # Out of bounds check
            if not (0 <= r < m and 0 <= c < n):
                return None
            
            # If it's a mirror, reflect immediately without entering the cell
            if grid[r][c] == 1:
                if direction == 0:  # Intended to move Right into a mirror -> Deflects Down
                    res = resolve_step(r + 1, c, 1)
                else:               # Intended to move Down into a mirror -> Deflects Right
                    res = resolve_step(r, c + 1, 0)
                memo[state] = res
                return res
            
            # Found an empty cell destination
            return (r, c, direction)

        # dp[r][c][dir]: total ways to be at empty cell (r, c) facing direction (0=Right, 1=Down)
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        # Initial step options from the starting point (0, 0)
        # Start by attempting to go right from (0,0) towards (0,1)
        step_right = resolve_step(0, 1, 0)
        if step_right:
            nr, nc, ndir = step_right
            dp[nr][nc][ndir] = (dp[nr][nc][ndir] + 1) % MOD
            
        # Start by attempting to go down from (0,0) towards (1,0)
        step_down = resolve_step(1, 0, 1)
        if step_down:
            nr, nc, ndir = step_down
            dp[nr][nc][ndir] = (dp[nr][nc][ndir] + 1) % MOD
            
        # Standard topological cell processing (valid because we only transition forward to empty cells)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                
                # Option A: Attempt to exit current cell by moving Right
                if dp[r][c][0] > 0 or dp[r][c][1] > 0:
                    ways_leaving = (dp[r][c][0] + dp[r][c][1]) % MOD
                    
                    # Try going Right to (r, c + 1)
                    next_right = resolve_step(r, c + 1, 0)
                    if next_right:
                        nr, nc, ndir = next_right
                        dp[nr][nc][ndir] = (dp[nr][nc][ndir] + ways_leaving) % MOD
                        
                    # Try going Down to (r + 1, c)
                    next_down = resolve_step(r + 1, c, 1)
                    if next_down:
                        nr, nc, ndir = next_down
                        dp[nr][nc][ndir] = (dp[nr][nc][ndir] + ways_leaving) % MOD

        # If the destination cell itself is a mirror, it's impossible to land on it validly
        if grid[m - 1][n - 1] == 1:
            return 0
            
        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD
