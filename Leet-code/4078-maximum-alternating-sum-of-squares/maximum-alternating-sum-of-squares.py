class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort elements by their squared values
        nums.sort(key=lambda x: x * x)
        
        n = len(nums)
        mid = n // 2
        
        # Sum squares of the second half minus sum squares of the first half
        s1 = sum(x * x for x in nums[:mid])
        s2 = sum(x * x for x in nums[mid:])
        
        return s2 - s1
