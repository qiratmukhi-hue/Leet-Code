from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        enhanced = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        enhanced.sort(key=lambda x: (x[1], x[0]))
        
        end_times = [x[1] for x in enhanced]
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = enhanced[i - 1]
            prev_j = bisect.bisect_left(end_times, l)
            
            for k in range(1, 5):
                skip_state = dp[i - 1][k]
                
                prev_neg_w, prev_indices = dp[prev_j][k - 1]
                use_state = (prev_neg_w - w, sorted(prev_indices + [orig_idx]))
                
                prev_k_state = dp[i][k - 1]
                
                dp[i][k] = min(skip_state, use_state, prev_k_state)
                
        return dp[n][4][1]