class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        
        # min_len[i] stores the minimum length of a valid subarray ending at or before index i
        min_len = [INF] * n
        
        left = 0
        current_sum = 0
        ans = INF
        best_so_far = INF
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window until current_sum <= target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                curr_len = right - left + 1
                
                # If there was a valid subarray completely before `left`, combine them
                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, curr_len + min_len[left - 1])
                    
                best_so_far = min(best_so_far, curr_len)
                
            min_len[right] = best_so_far
            
        return ans if ans != INF else -1
