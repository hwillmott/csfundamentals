class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                stack.append(-stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if abs(num1) > abs(num2):
                    stack.append(0)
                else:
                    stack.append(num2 // num1)
            else:
                stack.append(int(t))
            print(str(stack) + " " + str(t))
        return stack.pop()