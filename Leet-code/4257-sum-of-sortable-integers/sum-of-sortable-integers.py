class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        # Helper function to validate if a specific k works
        def check(k):
            prev_max = float('-inf')
            
            for start in range(0, n, k):
                # Count drops in the circular representation of the subarray
                drops = 0
                drop_idx = -1
                
                for i in range(k):
                    curr_val = nums[start + i]
                    next_val = nums[start + (i + 1) % k]
                    if curr_val > next_val:
                        drops += 1
                        drop_idx = i
                
                # If there is more than 1 drop, it cannot be cyclically sorted
                if drops > 1:
                    return False
                
                # Determine block min and max after optimal cyclic rotation
                if drops == 0:
                    # Array is already fully non-decreasing
                    b_min = nums[start]
                    b_max = nums[start + k - 1]
                else:
                    # Drop index is where nums[start + i] > nums[start + i + 1]
                    # The element after the drop becomes the start of the sorted block
                    b_min = nums[start + (drop_idx + 1) % k]
                    b_max = nums[start + drop_idx]
                
                # Verify cross-block ordering constraint
                if b_min < prev_max:
                    return False
                
                prev_max = b_max
                
            return True

        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        # Sum all sortable divisors
        for k in divisors:
            if check(k):
                ans += k
                
        return ans
