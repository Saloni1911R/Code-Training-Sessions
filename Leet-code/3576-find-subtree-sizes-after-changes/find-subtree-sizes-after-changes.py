import sys

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        sys.setrecursionlimit(max(sys.getrecursionlimit(), len(parent) + 10))
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        def assign_parents(u):
            c = ord(s[u]) - ord('a')
            prev = last[c]
            if prev != -1:
                new_parent[u] = prev
            last[c] = u
            for v in adj[u]:
                assign_parents(v)
            last[c] = prev

        assign_parents(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def calc_sizes(u):
            size = 1
            for v in new_adj[u]:
                size += calc_sizes(v)
            ans[u] = size
            return size

        calc_sizes(0)
        return ans
