class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
    
        def DFS(position):
            if position >= len(nums):
                ans.append(subset.copy())
                return 
            subset.append(nums[position])
            DFS(position + 1)

            subset.pop()
            DFS(position + 1)
        
        DFS(0)
        return ans
            
