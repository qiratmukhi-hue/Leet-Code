class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Base Cases
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        
        f3, f2, f1 = 5, 2, 1
        
        for i in range(4, n + 1):
            curr = (2 * f3 + f1) % MOD
            f1, f2, f3 = f2, f3, curr
            
        return f3