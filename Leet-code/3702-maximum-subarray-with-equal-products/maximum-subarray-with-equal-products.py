from fractions import gcd


class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        ans = 0

        total_lcm = 1
        for x in nums:
            total_lcm = lcm(total_lcm, x)
        max_bound = total_lcm * max(nums)

        for i in range(n):
            prod = 1
            l = 1
            g = 0
            for j in range(i, n):
                prod *= nums[j]
                if prod > max_bound:
                    break
                l = lcm(l, nums[j])
                g = gcd(g, nums[j])
                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans
