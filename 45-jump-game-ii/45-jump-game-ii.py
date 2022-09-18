class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 2
        goal = len(nums) - 1
        stepsTaken = 0
        while i >= 0 and goal != 0:
            furthest_step_backwards = goal
            for j in range(i, -1, -1):
                if j + nums[j] >= goal:
                    furthest_step_backwards = min(furthest_step_backwards, j)
            goal = furthest_step_backwards
            stepsTaken += 1
            i = goal - 1
            
        return stepsTaken