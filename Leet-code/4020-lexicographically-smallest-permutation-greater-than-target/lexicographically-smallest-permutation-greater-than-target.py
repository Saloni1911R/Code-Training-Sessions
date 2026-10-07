from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        s_counts = Counter(s)
        
        # Iterate backwards to find the maximum possible matching prefix length
        for i in range(n - 1, -1, -1):
            prefix = target[:i]
            prefix_counts = Counter(prefix)
            
            # Check if 's' has enough characters to form the target's prefix
            possible = True
            rem_counts = Counter(s_counts)
            for char, count in prefix_counts.items():
                if rem_counts[char] < count:
                    possible = False
                    break
                rem_counts[char] -= count
                
            if not possible:
                continue
                
            # Find the smallest available character strictly greater than target[i]
            target_char = target[i]
            chosen_char = None
            for c in sorted(rem_counts.keys()):
                if c > target_char and rem_counts[c] > 0:
                    chosen_char = c
                    break
            
            # If a valid character is found, construct the smallest remaining suffix
            if chosen_char:
                rem_counts[chosen_char] -= 1
                suffix = []
                for c in sorted(rem_counts.keys()):
                    suffix.append(c * rem_counts[c])
                
                return prefix + chosen_char + "".join(suffix)
                
        return ""
