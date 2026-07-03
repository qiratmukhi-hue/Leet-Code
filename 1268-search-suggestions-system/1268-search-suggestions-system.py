class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :type rtype: List[List[str]]
        """
        products.sort()
        res = []
        left = 0
        right = len(products) - 1
        
        for i in range(len(searchWord)):
            char = searchWord[i]
            
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1
                
            suggestions = []
            for j in range(left, min(left + 3, right + 1)):
                suggestions.append(products[j])
            res.append(suggestions)
            
        return res