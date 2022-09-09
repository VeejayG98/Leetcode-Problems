from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            word_dict[key].append(word)
        
        return [collection for collection in word_dict.values()]