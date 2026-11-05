class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def backtrack(start,path):
            if start==len(s):
                path_copy=path.copy()
                result.append(path_copy)
                return 
            
            for end in range(start+1,len(s)+1):

                sub=s[start:end]

                if sub!=sub[::-1]:
                    continue
                path.append(sub)

                backtrack(end,path)
                path.pop()
        backtrack(0,[])
        return result
        