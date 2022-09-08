class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         print(set(nums))
#         nums = list(set(nums))
#         print(nums)
#         count = 1
#         maxCount = 0
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1] + 1:
#                 count += 1
#                 print(count, nums[i])
#             else:
#                 maxCount = max(maxCount, count)
        
#         return max(maxCount, count)
        
            
        
        # print(sorted(nums))
        # print(set(nums))
        longest_seq = {}
        largest_num = -math.inf
        for num in nums:
            # print(num)
            if num in longest_seq:
                continue
            if num - 1 in longest_seq and num + 1 in longest_seq:
                longest_seq[num] = longest_seq[num + 1] + 1
                # longest_seq[num - 1] = longest_seq[num] + 1
                while num - 1 in longest_seq:
                    longest_seq[num - 1] = longest_seq[num] + 1
                    num = num - 1
            elif num - 1 in longest_seq:
                longest_seq[num] = longest_seq[num - 1]
                # longest_seq[num - 1] += 1
                while num - 1 in longest_seq:
                    longest_seq[num - 1] += 1
                    num = num - 1
            elif num + 1 in longest_seq:
                longest_seq[num] = longest_seq[num + 1] + 1
            else:
                longest_seq[num] = 1
            largest_num = max(largest_num, num)
            # print(longest_seq)
            # print(sorted(longest_seq.keys()))
        # print(max(longest_seq.values()))
        return max(longest_seq.values()) if longest_seq else 0
