class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_string = ""
        for character in s:
            if character.isalpha():
                modified_string += character.lower()
            elif character.isdigit():
                modified_string += character
        return modified_string == modified_string[:: -1]