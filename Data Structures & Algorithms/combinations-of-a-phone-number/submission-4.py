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
            letters=my_dict[digits[index]]
            for letter in letters:
                backtrack(index+1,sub+letter)
        backtrack(0,str())
        return result
        