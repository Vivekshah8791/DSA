class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch=="+":
                if len(stack)>=2:
                    second=stack.pop()
                    first=stack.pop()
                    op=first+second
                    stack.append(op)
            elif ch=="-":
                if len(stack)>=2:
                    second=stack.pop()
                    first=stack.pop()
                    op=first-second
                    stack.append(op)
            elif ch=='*':
                if len(stack)>=2:
                    second=stack.pop()
                    first=stack.pop()
                    op=first*second
                    stack.append(op)
                    
            elif ch=='/':
                if len(stack)>=2:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
            else:
                stack.append(int(ch))
        return stack[0]



