class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        if len(tokens) == 1:
            res = int(tokens[0])
        for token in tokens:
            operators = [ '+', '-', '*', '/']
            if stack and token in operators:
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                if token == "+":
                    res = oper1 + oper2
                elif token == "-":
                    res = oper2 - oper1
                elif token == "*":
                    res = oper2 * oper1
                elif token == "/":
                    res = int(oper2 / oper1)
                stack.append(res)
            else:
                stack.append(token)
        return res