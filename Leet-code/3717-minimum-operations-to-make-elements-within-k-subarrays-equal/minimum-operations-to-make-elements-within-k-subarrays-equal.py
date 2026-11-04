from sortedcontainers import SortedList

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        window_cost = [0] * (n - x + 1)
        
        lower = SortedList()
        upper = SortedList()
        lower_sum = 0
        upper_sum = 0
        
        # The lower half needs to hold the median at its maximum element
        lower_target_size = (x + 1) // 2
        
        # Step 1: Compute the L1 cost for every window of size x
        for i in range(n):
            v = nums[i]
            if not lower or v <= lower[-1]:
                lower.add(v)
                lower_sum += v
            else:
                upper.add(v)
                upper_sum += v
                
            # Remove the element falling out of the window
            if i >= x:
                out = nums[i - x]
                if out in lower:
                    lower.remove(out)
                    lower_sum -= out
                else:
                    upper.remove(out)
                    upper_sum -= out
            
            # Rebalance the two halves
            while len(lower) > lower_target_size:
                moved = lower.pop(-1)
                lower_sum -= moved
                upper.add(moved)
                upper_sum += moved
            while len(lower) < lower_target_size and upper:
                moved = upper.pop(0)
                upper_sum -= moved
                lower.add(moved)
                lower_sum += moved
                
            # Record the cost once a full window is formed
            if i >= x - 1:
                median = lower[-1]
                cost = (median * len(lower) - lower_sum) + (upper_sum - median * len(upper))
                window_cost[i - x + 1] = cost
                
        # Step 2: DP to select k non-overlapping windows with minimal total cost
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option 1: Skip the current element
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Form a valid subarray of size x ending at index i - 1
                if i >= x:
                    cost = window_cost[i - x]
                    if dp[i - x][j - 1] != INF:
                        if dp[i - x][j - 1] + cost < dp[i][j]:
                            dp[i][j] = dp[i - x][j - 1] + cost
                            
        return dp[n][k]
