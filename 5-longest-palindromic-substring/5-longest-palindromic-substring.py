class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = ""
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            odd_length = self.expandAroundCenter(s, i, i)
            even_length = self.expandAroundCenter(s, i, i + 1)
            max_length = max(odd_length, even_length, max_length, key = len)
            
        return max_length
        
    def expandAroundCenter(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1: end]
    
    