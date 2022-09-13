class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = ""
        
        if s == s[:: -1]:
            return s
        
        for i in reversed(range(-1, len(s) - 1)):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
            
                if dp[i][j]:
                    ans = max(ans, s[i: j + 1], key = len)
        
        return ans