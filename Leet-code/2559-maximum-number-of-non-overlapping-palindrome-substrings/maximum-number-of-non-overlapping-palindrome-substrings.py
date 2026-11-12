class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        count = 0
        i = 0
        while i < n:
            # Check palindrome of length k ending at i + k - 1
            if i + k <= n and is_palindrome(i, i + k - 1):
                count += 1
                i += k
            # Check palindrome of length k + 1 ending at i + k
            elif i + k + 1 <= n and is_palindrome(i, i + k):
                count += 1
                i += k + 1
            else:
                i += 1
                
        return count
