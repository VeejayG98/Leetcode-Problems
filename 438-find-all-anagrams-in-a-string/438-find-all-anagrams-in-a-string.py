class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        key_p = [0] * 26
        for letter in p:
            key_p[ord(letter) - ord('a')] += 1
            
        ans = []
        key_s = [0] * 26
        for i in range(len(s)):
            letter = s[i]
            key_s[ord(letter) - ord('a')] += 1
            
            if i >= len(p):
                key_s[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if key_s == key_p:
                ans.append(i - len(p) + 1)
        return ans