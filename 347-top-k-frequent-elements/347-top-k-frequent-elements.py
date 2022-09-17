class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return heapq.nlargest(k, freq.keys(), freq.get)