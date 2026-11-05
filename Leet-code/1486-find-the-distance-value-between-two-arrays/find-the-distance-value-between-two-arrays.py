import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the first element in arr2 greater than or equal to x - d
            idx = bisect.bisect_left(arr2, x - d)
            
            # If such an element exists and it is also less than or equal to x + d,
            # then we found an element within the invalid range.
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
                
            distance_value += 1
            
        return distance_value
