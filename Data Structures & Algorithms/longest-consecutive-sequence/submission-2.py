class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        seen=set()
        for num in nums:
            seen.add(num)
        final=1
        for num in nums:
            count=1
            if num-1 in seen:
                continue
            elif num+1 in seen:
                count+=1
                look=num+2
                while look in seen:
                    count+=1
                    look+=1
            else:
                count=1
            final=max(final,count)
        return final
        
        