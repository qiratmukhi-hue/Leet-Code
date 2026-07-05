class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :type rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, target, path):
            if len(path) == k:
                if target == 0:
                    res.append(list(path))
                return
            
            if target < 0 or len(path) > k:
                return
                
            for i in range(start, 10):
                if i > target:
                    break
                path.append(i)
                backtrack(i + 1, target - i, path)
                path.pop()
                
        backtrack(1, n, [])
        return res