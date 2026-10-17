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
            left=i+1
            right=len(nums)-1
            while left<right:
                if left>i+1 and nums[left]==nums[left-1]:
                    left+=1
                    continue
                elif right<(len(nums)-1) and nums[right]==nums[right+1]:
                    right-=1
                    continue
                else:
                    sum=nums[left]+nums[right]
                    if sum==target:
                        result.append([nums[i],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif sum<target:
                        left+=1
                    else:
                        right-=1
        return result
        