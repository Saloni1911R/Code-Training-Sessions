class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        odd_count = 0
        even_count = 1  # Accounts for initial prefix sum of 0
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 1:
                result += even_count
                odd_count += 1
            else:
                result += odd_count
                even_count += 1
                
        return result % MOD
