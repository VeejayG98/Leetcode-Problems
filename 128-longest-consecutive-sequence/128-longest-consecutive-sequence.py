class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLongestSequence = 0
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                
                longestSequence = 1
                while num + 1 in nums:
                    longestSequence += 1
                    num += 1
            
                maxLongestSequence = max(maxLongestSequence, longestSequence)
        
        return maxLongestSequence