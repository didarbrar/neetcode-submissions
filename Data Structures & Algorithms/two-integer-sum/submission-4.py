class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums):
            required=target-num

            if required in seen:
                return ([seen[required],index])
            seen[num]=index
            
        