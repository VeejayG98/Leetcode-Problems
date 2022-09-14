class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = []
        count = 0
        for i in range(len(s)):
            count += self.expandAroundCenter(s, i, i)
            count += self.expandAroundCenter(s, i, i + 1)
        return count
    
    def expandAroundCenter(self, s, start, end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
        return count