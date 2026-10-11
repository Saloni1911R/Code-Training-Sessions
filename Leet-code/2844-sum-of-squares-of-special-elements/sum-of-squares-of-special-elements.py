class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                total_sum += nums[i - 1] ** 2
                
        return total_sum
