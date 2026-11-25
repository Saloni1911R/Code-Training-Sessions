class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        # Coordinate compress values to 0..m-1
        vals = sorted(set(nums))
        comp = {v: i for i, v in enumerate(vals)}
        s = [comp[x] for x in nums]

        # Build suffix array in O(n log^2 n)
        sa = list(range(n))
        rank = s[:]
        k = 1
        while k < n:
            sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
            tmp = [0] * n
            for i in range(1, n):
                a, b = sa[i - 1], sa[i]
                ra = (rank[a], rank[a + k] if a + k < n else -1)
                rb = (rank[b], rank[b + k] if b + k < n else -1)
                tmp[b] = tmp[a] + (1 if ra != rb else 0)
            rank = tmp
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1

        # Kasai's algorithm for LCP between adjacent suffixes in sa
        pos = [0] * n
        for idx, suffix_start in enumerate(sa):
            pos[suffix_start] = idx

        lcp = [0] * max(0, n - 1)
        h = 0
        for i in range(n):
            r = pos[i]
            if r == n - 1:
                h = 0
                continue
            j = sa[r + 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[r] = h
            if h > 0:
                h -= 1

        # Maximum LCP with any other suffix for each starting index i
        max_lcp = [0] * n
        for r, i in enumerate(sa):
            best = 0
            if r > 0:
                best = max(best, lcp[r - 1])
            if r < n - 1:
                best = max(best, lcp[r])
            max_lcp[i] = best

        ans = n
        for i in range(n):
            needed = max_lcp[i] + 1
            if i + needed <= n and needed < ans:
                ans = needed

        return ans
