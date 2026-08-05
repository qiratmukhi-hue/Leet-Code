from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
                    
        for u, v in invocations:
            if suspicious[v] and not suspicious[u]:
                return list(range(n))
                
        return [i for i in range(n) if not suspicious[i]]