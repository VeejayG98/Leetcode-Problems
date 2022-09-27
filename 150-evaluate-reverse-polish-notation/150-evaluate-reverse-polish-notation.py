class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+' : lambda a, b: a + b,
                     '*' : lambda a, b: a * b,
                     '/' : lambda a, b: int(a / b),
                     '-' : lambda a, b : a - b}
        stack = []
        for token in tokens:
            if token in operations:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = self.performOperation(operand1, operand2, operations[token])
                stack.append(result)
            else:
                stack.append(token)
        return stack.pop()
            
    def performOperation(self, operand1, operand2, function):
        return function(operand1, operand2)