import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        for num2, num1 in pairs:
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
                
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)
                
        return max_score