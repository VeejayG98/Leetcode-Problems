class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        for letter in t:
            if letter not in freq or freq[letter] < 1:
                return False
            freq[letter] -= 1
        return True