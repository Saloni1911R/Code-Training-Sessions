from collections import defaultdict

class Solution(object):
    def countServers(self, n, logs, x, queries):
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while preserving their original indices: (query_time, original_index)
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        cnt = defaultdict(int)
        
        left = 0
        right = 0
        m = len(logs)
        
        for orig_idx, q in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Expand right pointer to include logs <= window_end
            while right < m and logs[right][1] <= window_end:
                cnt[logs[right][0]] += 1
                right += 1
                
            # Shrink left pointer to remove logs < window_start
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                cnt[server_id] -= 1
                if cnt[server_id] == 0:
                    del cnt[server_id]
                left += 1
                
            # Total servers minus servers that received at least one request
            ans[orig_idx] = n - len(cnt)
            
        return ans
