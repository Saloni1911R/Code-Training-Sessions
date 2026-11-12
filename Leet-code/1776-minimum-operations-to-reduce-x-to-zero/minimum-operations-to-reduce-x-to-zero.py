class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        n = len(nums)
        
        # If target is negative, even removing all elements isn't enough
        if target < 0:
            return -1
            
        # If target is 0, we must remove all elements
        if target == 0:
            return n
            
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(n):
            current_sum += nums[right]
            
            # Shrink window from the left if current_sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return n - max_len if max_len != -1 else -1
