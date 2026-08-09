class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                stones = suffix_sum[i] - dp(i + X, max(M, X))
                max_stones = max(max_stones, stones)
                
            memo[(i, M)] = max_stones
            return max_stones
        
        return dp(0, 1)