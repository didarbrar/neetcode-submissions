class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result=nums[0]
        max_product=nums[0]
        min_product=nums[0]
        
        n=len(nums)

        for i in range(1,n):

            candidate=(nums[i],
            nums[i]*max_product,
            nums[i]*min_product)

            new_max=max(candidate)
            new_min=min(candidate)

            max_product=new_max
            min_product=new_min

            result=max(result,max_product)
            
        return result