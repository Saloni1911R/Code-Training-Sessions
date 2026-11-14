class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        min_positive_sum = float('inf')

        # Iterate over every possible starting index
        for i in range(n):
            current_sum = 0
            # Expand the subarray up to length r
            for j in range(i, min(n, i + r)):
                current_sum += nums[j]
                length = j - i + 1
                
                # Check if length is within [l, r] and sum is strictly positive
                if length >= l and current_sum > 0:
                    min_positive_sum = min(min_positive_sum, current_sum)

        return min_positive_sum if min_positive_sum != float('inf') else -1
