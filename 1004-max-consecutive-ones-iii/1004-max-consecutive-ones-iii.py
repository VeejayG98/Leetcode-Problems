class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longestSequence = 0
        i = 0
        j = 0
        zerosCount = 0
        
        while j < len(nums):
            if nums[j] == 0:
                zerosCount += 1
                # print(longestSequence, i , j)
            while zerosCount > k:
                if nums[i] == 0:
                    zerosCount -= 1
                i += 1
            longestSequence = max(longestSequence, j - i + 1)
            j += 1
        
        return longestSequence
            
        # return max(longestSequence, j - i)
        