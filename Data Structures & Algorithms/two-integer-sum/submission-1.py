class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts={}
        for i in range(0,len(nums)):
            num=nums[i]
            counts[target-num]=i
            for j in range(i+1,len(nums)):
                numb=nums[j]
                if numb in counts:
                    return[i,j]
        
        