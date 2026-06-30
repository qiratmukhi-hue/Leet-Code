class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for right, char in enumerate(s):
            last_pos[char] = right
            if last_pos['a'] != -1 and last_pos['b'] != -1 and last_pos['c'] != -1:
                count += min(last_pos['a'], last_pos['b'], last_pos['c']) + 1
                
        return count