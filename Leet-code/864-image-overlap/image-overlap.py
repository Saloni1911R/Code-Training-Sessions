from collections import Counter

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        # Get coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count the occurrences of each translation vector
        transformation_counts = Counter()
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Calculate the exact displacement vector
                vector = (r2 - r1, c2 - c1)
                transformation_counts[vector] += 1
                
        # The maximum frequency gives the largest overlap
        return max(transformation_counts.values()) if transformation_counts else 0
