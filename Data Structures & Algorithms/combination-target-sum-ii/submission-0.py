class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start,sum,sub):
            if sum>target:
                return
            if sum==target:
                sub_copy=sub.copy()
                result.append(sub_copy)
                return 
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                sum+=candidates[i]
                sub.append(candidates[i])
                backtrack(i+1,sum,sub)
                last=sub.pop()
                sum-=last
        backtrack(0,0,[])
        return result
        