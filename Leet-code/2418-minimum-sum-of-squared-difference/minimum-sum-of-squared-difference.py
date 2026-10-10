class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        # 1. Calculate absolute differences
        diffs = [abs(x - y) for x, y in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        # If there are no differences, sum of squares is already 0
        if max_diff == 0:
            return 0
            
        # 2. Count frequencies of each difference using buckets
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
            
        # Total operations available across both arrays
        k = k1 + k2
        
        # 3. Greedily reduce the largest differences from top to bottom
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
                
            # If k can completely reduce all elements of current diff 'd' to 'd-1'
            if k >= buckets[d]:
                k -= buckets[d]
                buckets[d - 1] += buckets[d]
                buckets[d] = 0
            else:
                # If k cannot reduce all, reduce as many as possible
                buckets[d - 1] += k
                buckets[d] -= k
                k = 0
                break
                
        # 4. Calculate the final sum of squared differences
        return sum(count * (d ** 2) for d, count in enumerate(buckets))
