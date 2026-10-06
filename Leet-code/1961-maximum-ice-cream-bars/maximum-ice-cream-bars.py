class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        freq = [0] * 100001
        
        for cost in costs:
            freq[cost] += 1
            
        count = 0
        for cost in range(1, 100001):
            if freq[cost] == 0:
                continue
                
            if coins < cost:
                break
            bars_to_buy = min(freq[cost], coins // cost)
            count += bars_to_buy
            coins -= bars_to_buy * cost
            
        return count