class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0
        
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j]:
                    count += 1
        return count