class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start,sum,sub):
            if sum>target:
                return
            if sum==target:
                sub_copy=sub.copy()
                result.append(sub_copy)
                return 
            for i in range(start,len(nums)):
                sum+=nums[i]
                sub.append(nums[i])
                backtrack(i,sum,sub)
                last=sub.pop()
                sum-=last
        backtrack(0,0,[])
        return result
            


        