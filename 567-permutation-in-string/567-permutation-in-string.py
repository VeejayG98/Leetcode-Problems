class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key_s1 = [0] * 26
        freq = {}
        for letter in s1:
            key_s1[ord(letter) - ord('a')] += 1
            freq[letter] = freq.get(letter, 0) + 1
        key_s2 = [0] * 26
        i = 0
        j = 0
        while i < len(s2) and j < len(s2):
            letter = s2[j]
            key_s2[ord(letter) - ord('a')] += 1
            
            if letter not in freq or freq[letter] == 0:
                key_s2[ord(s2[i]) - ord('a')] -= 1
                i += 1
            else:
                freq[letter] -= 1
            
            if key_s1 == key_s2:
                return True
            j += 1
        return False
    # def getKey(self, s):
    #     key = [0] * 26
    #     for letter in s:
    #         key[ord(letter) - ord('a')] += 1
    #     return key