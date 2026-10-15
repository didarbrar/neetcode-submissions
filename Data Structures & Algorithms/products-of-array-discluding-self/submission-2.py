class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1 for _ in range(len(nums))]
        prefix=[1 for _ in range(len(nums))]
        suffix=[1 for _ in range(len(nums))]
        n=len(nums)
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        for i in range(len(nums)):
            output[i]=prefix[i]*suffix[i]
        return output       
                        