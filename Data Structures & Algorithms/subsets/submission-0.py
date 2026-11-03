class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index,sub):
            sub_copy=sub.copy()
            result.append(sub_copy)
            for i in range(index,len(nums)):
                sub.append(nums[i])
                backtrack(i+1,sub)
                sub.pop()

        backtrack(0,[])
        return result

        
        