class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        result=[]
        for num in nums:
            if num not in my_dict:
                my_dict[num]=0
            my_dict[num]+=1
        
        bucket=[[] for _ in range(len(nums)+1)]

        for num,count in my_dict.items():
            bucket[count].append(num)
        
        for count in range(len(nums),0,-1):
            for num in bucket[count]:
                result.append(num)
            
            if len(result)==k:
                return result
        return result
        
        