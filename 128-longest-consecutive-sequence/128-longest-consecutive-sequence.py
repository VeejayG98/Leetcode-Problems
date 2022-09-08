class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_seq = {}
        for num in nums:
            if num in longest_seq:
                continue
            if num - 1 in longest_seq and num + 1 in longest_seq:
                longest_seq[num] = longest_seq[num + 1] + 1
                while num - 1 in longest_seq:
                    longest_seq[num - 1] = longest_seq[num] + 1
                    num = num - 1
            elif num - 1 in longest_seq:
                longest_seq[num] = longest_seq[num - 1]
                while num - 1 in longest_seq:
                    longest_seq[num - 1] += 1
                    num = num - 1
            elif num + 1 in longest_seq:
                longest_seq[num] = longest_seq[num + 1] + 1
            else:
                longest_seq[num] = 1
        return max(longest_seq.values()) if longest_seq else 0
