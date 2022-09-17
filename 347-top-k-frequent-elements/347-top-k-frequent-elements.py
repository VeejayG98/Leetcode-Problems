class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = [(-v, k) for k, v in freq.items()]
        heapq.heapify(freq)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq)[1])
        return ans