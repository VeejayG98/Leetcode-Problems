from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            alphabets = [0] * 26
            for letter in word:
                alphabets[ord(letter) - ord('a')] += 1
            word_dict[tuple(alphabets)].append(word)
        return word_dict.values()