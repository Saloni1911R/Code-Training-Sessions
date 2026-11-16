class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Continue performing rounds while the string length exceeds k
        while len(s) > k:
            next_s = []
            
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                group = s[i:i + k]
                
                # Calculate the sum of digits in the current group
                group_sum = sum(int(char) for char in group)
                
                # Append the string representation of the sum
                next_s.append(str(group_sum))
                
            # Merge the new groups to form the updated string s
            s = "".join(next_s)
            
        return s
