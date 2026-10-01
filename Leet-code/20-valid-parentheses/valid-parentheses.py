class Solution(object):

    def isValid(self, s):
        """

        :type s: str

        :rtype: bool

        """
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                # If stack has elements, pop the top element; otherwise use a dummy value
                top_element = stack.pop() if stack else "#"

                # Check if the popped opening bracket matches the expected pair
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # String is valid only if all brackets were properly matched and popped
        return not stack