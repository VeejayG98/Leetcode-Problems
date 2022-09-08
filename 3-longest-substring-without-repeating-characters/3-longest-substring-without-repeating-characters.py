class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        i = 0
        j = 0
        maxLength = 0
        
        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0) + 1
            
            while freq[s[j]] > 1:
                freq[s[i]] -= 1
                i += 1
            maxLength = max(maxLength, j - i + 1)
            j += 1
        return maxLength