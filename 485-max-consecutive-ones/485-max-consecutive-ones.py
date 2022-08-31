class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_win_len = 0
        i = 0
        j = 0
        while i < len(nums):
            if j == len(nums):
                max_win_len = max(j - i, max_win_len)
                break
            if nums[j] == 1:
                j += 1
            else:
                # print(i, j, j - i)
                max_win_len = max(j - i, max_win_len)
                j += 1
                i = j
        
        return max_win_len