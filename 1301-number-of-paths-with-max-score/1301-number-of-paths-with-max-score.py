class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                curr_val = 0 if board[r][c] == 'E' else int(board[r][c])
                max_sum = -1
                paths = 0
                
                directions = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                
                for nr, nc in directions:
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        neighbor_sum, neighbor_paths = dp[nr][nc]
                        candidate_sum = neighbor_sum + curr_val
                        
                        if candidate_sum > max_sum:
                            max_sum = candidate_sum
                            paths = neighbor_paths
                        elif candidate_sum == max_sum:
                            paths = (paths + neighbor_paths) % MOD
                
                if max_sum != -1:
                    dp[r][c] = [max_sum, paths]
                    
        ans = dp[0][0]
        return [ans[0], ans[1]] if ans[0] != -1 else [0, 0]