class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        # Case 1: The entire array has a non-zero XOR sum
        if total_xor != 0:
            return len(nums)
            
        # Case 2: Total XOR is 0, but we can drop one non-zero element
        if has_nonzero:
            return len(nums) - 1
            
        # Case 3: Every single element is 0
        return 0
