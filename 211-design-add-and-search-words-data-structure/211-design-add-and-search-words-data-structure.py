"""["WordDictionary","addWord","search", "addWord","addWord","search","search","addWord","search","addWord","search","addWord","addWord","search","addWord","addWord","search"]
[[],["xgvk"],[".gvk"],["wykzbvwdsoyfowqicymzd"],["xajbtjyjuwgoynjgu"],["wykzbvwdso..owqicymzd"],["..ha"],["qsibzxaorktypkfg"],["xgvk"],["vbycuvrkbcq"],["qsibz.aorkty.kfg"],["sm"],["fkqclfmvzpzpnbvz"],["vb..uvrkbcq"],["jpnneostllnnma"],["zvmtfg"],[".gvk"]]
"""


class DictNode:
    def __init__(self, char = ""):
        self.val = char
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = DictNode(char)
                node.children[char] = new_node
                node = new_node
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        print(word, node.children.keys())
        return self.searchHelper(word, 0, node)
        # isFound = False
        # while i < len(word) and not isFound:
        #     char = word[i]
        #     if char == '.':
        #         for key in node.children.keys():
        #             isFound = self.search(word[])
        #             if isFound:
        #                 return True
                    
    def searchHelper(self, subWord, i, node):
        isFound = False
        while i < len(subWord) and not isFound:
            char = subWord[i]
            if len(node.children) == 0:
                return False
            
            if char == '.':
                # print(subWord, node.val)
                if len(node.children) != 0:
                    # print(node.children.keys())
                    for key in node.children.keys():
                        isFound = self.searchHelper(subWord, i + 1, node.children[key])
                        if isFound:
                            return isFound
                else:
                    return True
            if char not in node.children:
                return False
            
            node = node.children[char]
            i += 1
        return node.isWord if i == len(subWord) else False
            
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)