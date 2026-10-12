class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :type rtype: int
        """
        MOD = 10**9 + 7
        # There are 31 bits needed to represent up to 10^9
        bit_counts = [0] * 31
        
        # Count the occurrences of each bit position
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        
        # Greedily construct the k largest numbers
        for _ in range(k):
            current_num = 0
            for i in range(31):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the constructed number to the total sum
            ans = (ans + current_num * current_num) % MOD
            
        return ans
