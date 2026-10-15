class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for num in nums:
            if num not in my_dict:
                my_dict[num]=0
            my_dict[num]+=1
        
        top_k=sorted(my_dict,key=my_dict.get,reverse=True)[:k]
        return top_k
        