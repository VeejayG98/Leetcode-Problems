class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        maxLength = 0
        freq = {}
        maxFreq = 0
        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxFreq = max(maxFreq, freq[s[j]])
            if (j - i + 1) - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            maxLength = max(maxLength, j - i + 1)
            j += 1
        return maxLength