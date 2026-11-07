import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # idle heap: stores (weight, server_index)
        idle = []
        for i, w in enumerate(servers):
            heapq.heappush(idle, (w, i))
            
        # busy heap: stores (free_time, weight, server_index)
        busy = []
        ans = [0] * len(tasks)
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            curr_time = max(curr_time, j)
            
            # Free up servers whose finish time <= curr_time
            while busy and busy[0][0] <= curr_time:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(idle, (w, i))
                
            # If no server is idle, fast-forward time to the next available server
            if not idle:
                curr_time = busy[0][0]
                while busy and busy[0][0] <= curr_time:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(idle, (w, i))
                    
            # Assign task to the top idle server
            w, i = heapq.heappop(idle)
            ans[j] = i
            heapq.heappush(busy, (curr_time + task_time, w, i))
            
        return ans
