class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(sub,seen):
            if len(sub)==len(nums):
                sub_copy=sub.copy()
                result.append(sub_copy)
                return 
            for num in nums:
                if num in seen:
                    continue
                sub.append(num)
                seen.add(num)
                backtrack(sub,seen)
                last=sub.pop()
                seen.remove(last)
        backtrack([],set())
        return result
            
            