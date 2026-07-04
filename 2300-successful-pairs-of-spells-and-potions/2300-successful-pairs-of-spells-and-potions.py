class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            required = (success + spell - 1) // spell
            
            low = 0
            high = m
            while low < high:
                mid = (low + high) // 2
                if potions[mid] >= required:
                    high = mid
                else:
                    low = mid + 1
                    
            pairs.append(m - low)
            
        return pairs