class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        list1=nums[:-1]
        list2=nums[1:]

        def rob_1(nums: List[int]) -> int:
            rob=[0 for _ in range(len(nums))]
            rob[0]=nums[0]
            rob[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                rob[i]=max(rob[i-1],rob[i-2]+nums[i])
            return rob[len(nums)-1]
        
        first=rob_1(list1)
        second=rob_1(list2)

        return max(first,second)

        
        