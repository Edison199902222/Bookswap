class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        for c in expression:
            if c == ",":
                continue
            elif c == "t":
                stack.append(True)
            elif c == "f":
                stack.append(False)
            elif c in ['&', '|', '!', '(']:
                stack.append(c)
            elif c == ")":
                operation = []
                while stack and stack[-1] != "(":
                    operation.append(stack.pop())
                stack.pop()  # pop out '('.
                operater = stack.pop()  # pop out sign
                if operater == "&":
                    stack.append(all(operation))
                elif operater == "|":
                    stack.append(any(operation))
                elif operater == "!":
                    stack.append(not operation[0])
        return stack.pop()

