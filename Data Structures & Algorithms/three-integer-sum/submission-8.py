class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)) :
            if nums[i]>0:
                return result
            elif i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            seen=set()
            for j in range(i+1,len(nums)):
                required=target-nums[j]

                if required in seen:
                    subset=[nums[i],nums[j],required]
                    if subset not in result:
                         result.append([nums[i],nums[j],required])
                seen.add(nums[j])

        return result
        