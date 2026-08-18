class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_counts = defaultdict(int)
        
        for i in range(n - k + 1):
            sub = nums[i : i + k]
            
            for val in set(sub):
                subarray_counts[val] += 1
                
        ans = -1
        for val, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, val)
                
        return ans