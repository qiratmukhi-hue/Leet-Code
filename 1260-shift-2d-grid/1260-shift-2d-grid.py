class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                current_1d = r * n + c
                
                new_1d = (current_1d + k) % total
                
                new_r = new_1d // n
                new_c = new_1d % n
                result[new_r][new_c] = grid[r][c]
                
        return result