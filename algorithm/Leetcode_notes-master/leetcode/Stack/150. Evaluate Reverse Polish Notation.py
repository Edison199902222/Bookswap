class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                prev1 = stack.pop()
                prev2 = stack.pop()
                stack.append(self.caculate(prev2, prev1, tokens[i]))
            else:
                stack.append(int(tokens[i]))

        return sum(stack)

    def caculate(self, i, j, op):
        if op == "+":
            return i + j
        elif op == "-":
            return i - j
        elif op == "*":
            return i * j
        # 防止 6/-132 会等于-1， 应该等于0
        # 所以用float 进行计算后，int 取整
        elif op == "/":
            return int(i / j)