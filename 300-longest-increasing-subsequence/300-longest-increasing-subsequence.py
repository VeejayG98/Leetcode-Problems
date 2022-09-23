class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        ans = []
        for i in range(len(nums)):
                position = bisect_left(ans, nums[i])
                if position == len(ans):
                    ans.append(nums[i])
                else:
                    ans[position] = nums[i]
        return len(ans)