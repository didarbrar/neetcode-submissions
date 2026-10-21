class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number=[]
        operator = {'+', '-', '*', '/'}
        add='+'
        sub='-'
        mul='*'
        div='/'
        for i in range(len(tokens)):
            ch=tokens[i]
            if ch not in operator:
                number.append(int(ch))
            else:
                if ch==add:
                    number[-2]=(number[-2]+number[-1])
                    number.pop()
                elif ch==sub:
                    number[-2]=(number[-2]-number[-1])
                    number.pop()
                elif ch==mul:
                    number[-2]=(number[-2]*number[-1])
                    number.pop()
                else:
                    number[-2]=int(number[-2]/number[-1])
                    number.pop()
        return number[-1]
