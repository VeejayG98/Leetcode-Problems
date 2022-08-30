class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = [False] *(len(nums) + 1)
        for num in nums:
            ans[num] = True
        for res in range(len(ans)):
            if ans[res] == False:
                return res