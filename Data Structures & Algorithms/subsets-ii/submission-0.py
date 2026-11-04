class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def backtrack(index,sub):
            sub_copy=sub.copy()
            result.append(sub_copy)
            for i in range(index,len(nums)):
                if i >index and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                backtrack(i+1,sub)
                sub.pop()

        backtrack(0,[])
        return result
        