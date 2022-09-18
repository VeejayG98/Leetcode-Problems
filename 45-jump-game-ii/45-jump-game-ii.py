class Solution:
    def jump(self, nums: List[int]) -> int:
        currentJump = 0
        start = 0
        furthestJump = 0
        jumps = 0
        
        for i in range(len(nums) - 1):
            
            currentJump = max(currentJump, nums[i] + i)
            if i == furthestJump:
                jumps += 1
                furthestJump = currentJump
        
        return jumps
            