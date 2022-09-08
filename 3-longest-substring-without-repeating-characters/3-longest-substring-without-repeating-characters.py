class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        i = 0
        j = 1
        maxLength = 0
        
        if len(s) == 0:
            return maxLength
        if len(s) == 1:
            return 1
        
        freq[s[i]] = 1
        
        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            while freq[s[j]] > 1:
                maxLength = max(maxLength, j - i)
                # print(maxLength, i, j)
                freq[s[i]] -= 1
                i += 1
            j += 1
        return max(maxLength, j - i)