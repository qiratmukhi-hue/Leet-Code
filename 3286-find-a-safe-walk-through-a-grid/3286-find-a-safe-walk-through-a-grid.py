from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        
        dist[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    ncost = dist[r][c] + grid[nr][nc]
                    
                    if ncost < dist[nr][nc]:
                        dist[nr][nc] = ncost
                        
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        return dist[m-1][n-1] < health