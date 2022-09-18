class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = set()
        
        for i in range(len(nums)):
            if nums[i] in duplicates:
                return True
            duplicates.add(nums[i])
            if len(duplicates) > k:
                duplicates.remove(nums[i - k])
        return False            