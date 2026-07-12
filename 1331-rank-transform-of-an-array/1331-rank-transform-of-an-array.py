class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {}
        for rank, val in enumerate(sorted(set(arr)), 1):
            ranks[val] = rank
            
        return [ranks[num] for num in arr]