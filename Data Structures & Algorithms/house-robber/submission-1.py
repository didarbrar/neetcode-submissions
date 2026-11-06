class Solution:
    def rob(self, nums: List[int]) -> int:
        rob=[0 for _ in range(len(nums))]
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        rob[0]=nums[0]
        rob[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            rob[i]=max(rob[i-1],rob[i-2]+nums[i])
        return rob[len(nums)-1]

        