class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Helper function to compute the sum of digits of a number
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # Store elements along with their original index
        # Each entry: (digit_sum, value, original_index)
        arr = []
        for i, val in enumerate(nums):
            arr.append((get_digit_sum(val), val, i))
            
        # Sort based on custom criteria:
        # 1. By digit sum (ascending)
        # 2. By the number itself if digit sums are equal (ascending)
        arr.sort()
        
        # Use a visited array to keep track of cycle elements
        n = len(nums)
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct sorted position
            if visited[i] or arr[i][2] == i:
                continue
                
            # Calculate the cycle length
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]  # Move to the original index of the current element
                cycle_size += 1
                
            # A cycle of length L requires (L - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps
