class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        zerosCount = 0
        maxCount = 0
        
        while j < len(nums):
            
            if nums[j] == 0:
                zerosCount += 1
                # print(maxCount, i, j)
                
                while zerosCount > 1:
                    if nums[i] == 0:
                        zerosCount -= 1
                    i += 1
                    maxCount = max(maxCount, j - i + 1)
            j += 1
        
        return max(maxCount, j - i)