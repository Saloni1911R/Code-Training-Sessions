class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        
        # Precompute divisors for each length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        def get_cost(i, j):
            length = j - i + 1
            min_c = float('inf')
            for d in divisors[length]:
                curr_c = 0
                for group in range(d):
                    l, r = i + group, i + length - d + group
                    while l < r:
                        if s[l] != s[r]:
                            curr_c += 1
                        l += d
                        r -= d
                min_c = min(min_c, curr_c)
            return min_c

        for i in range(n):
            for j in range(i, n):
                cost[i][j] = get_cost(i, j)
                
        # dp[i][j] = min changes to partition s[0..i] into j substrings
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = cost[0][i]
            
        for j in range(2, k + 1):
            for i in range(j - 1, n):
                for p in range(j - 2, i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p + 1][i])
                    
        return dp[n - 1][k]
