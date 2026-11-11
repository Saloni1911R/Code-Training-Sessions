class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # Number of units where both requirements overlap
        common = min(need1, need2)
        
        # Best cost to satisfy the overlapping portion
        cost_common = common * min(costBoth, cost1 + cost2)
        
        # Remaining units needed for each type individually
        rem1 = need1 - common
        rem2 = need2 - common
        
        # Best cost for remaining units (Type 3 could still be cheaper than Type 1 or 2)
        cost_rem1 = rem1 * min(cost1, costBoth)
        cost_rem2 = rem2 * min(cost2, costBoth)
        
        return cost_common + cost_rem1 + cost_rem2
