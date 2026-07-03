from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            unique_costs.add(cost)
            
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo = []
        
        while queue:
            u = queue.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        candidates = sorted(list(unique_costs))
        ans = -1
        low = 0
        high = len(candidates) - 1
        
        while low <= high:
            mid = (low + high) // 2
            min_req = candidates[mid]
            
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo:
                if dist[u] != float('inf') and online[u]:
                    for v, cost in adj[u]:
                        if cost >= min_req and online[v]:
                            if dist[u] + cost < dist[v]:
                                dist[v] = dist[u] + cost
                                
            if dist[n - 1] <= k:
                ans = min_req
                low = mid + 1
            else:
                high = mid - 1
                
        return ans