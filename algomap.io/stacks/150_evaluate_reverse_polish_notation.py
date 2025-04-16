class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OP = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in OP:
                stack.append(int(token))
            else:
                r = stack.pop()
                l = stack.pop()
                match token:
                    case '+':
                        stack.append(l + r)
                    case '*':
                        stack.append(l * r)
                    case '-':
                        stack.append(l - r)
                    case '/':
                        stack.append(int(l / r))
        return stack[0]