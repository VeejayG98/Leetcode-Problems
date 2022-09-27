class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key_s1 = [0] * 26
        for letter in s1:
            key_s1[ord(letter) - ord('a')] += 1
        key_s2 = [0] * 26
        for i in range(len(s2)):
            letter = s2[i]
            key_s2[ord(letter) - ord('a')] += 1
            
            if i >= len(s1):
                key_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if key_s1 == key_s2:
                return True
        return False