class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        return sum(mx - num for num in nums)