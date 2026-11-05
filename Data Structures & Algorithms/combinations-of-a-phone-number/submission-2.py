class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        my_dict={
            '2':'abc','3':'def','4':'ghi',
            '5':'jkl','6':'mno','7':'pqrs',
            '8':'tuv','9':'wxyz'
        }
        result=[]
        n=len(digits)
        def backtrack(index,sub):
            if index==len(digits):
                sub_copy=sub
                result.append(sub_copy)
                return
            num=digits[index]
            letters=my_dict[num]
            for digit in letters:
                sub+=digit
                index+=1
                backtrack(index,sub)
                index-=1
                sub=sub[:-1]
        backtrack(0,str())
        return result
        