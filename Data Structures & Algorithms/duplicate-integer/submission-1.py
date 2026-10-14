class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dummy={}
        for index,num in enumerate(nums):
            if num in dummy:
                return True
            dummy[num]=index
        return False