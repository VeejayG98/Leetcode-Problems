class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}
        
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates[nums[i]] = i
            else:
                if i - duplicates[nums[i]] <= k:
                    return True
                else:
                    duplicates[nums[i]] = i
        return False