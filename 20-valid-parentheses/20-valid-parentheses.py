class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbol_dict = {')': '(',
                      '}' : '{',
                      ']': '['}
        for symbol in s:
            if symbol == '(' or symbol == '{' or symbol == '[':
                stack.append(symbol)
            elif not stack or stack.pop() != symbol_dict[symbol]:
                return False
        return True if len(stack) == 0 else False