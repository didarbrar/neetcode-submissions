class Solution:
    def isValid(self, s: str) -> bool:
        my_dict={')':'(',']':'[','}':'{'}
        open=[]
        if len(s)==1:
            return False
        for ch in s:
            if ch not in my_dict:
                open.append(ch)
            elif ch in my_dict:
                if not open or open[-1]!=my_dict[ch]:
                    return False
                else:
                    open.pop()
        return len(open)==0