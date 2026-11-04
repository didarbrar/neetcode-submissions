class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(open,close,s):
             if open>n:
                return
             if close>open:
                return
        
             if len(s)==2*n:
                result.append(s)
                return
             for ch in ['(',')']:
                s+=ch
                if ch=='(':
                    open+=1
                else:
                    close+=1
                backtrack(open,close,s)
                last=s[-1]
                s=s[:-1]
                if last=='(':
                    open-=1
                else:
                    close-=1
        backtrack(0,0,str())
        return result
                
            