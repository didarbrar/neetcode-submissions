class Solution:
    def countSubstrings(self, s: str) -> int:

        count=0

        def expand(left:int,right:int):
            temp_count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                temp_count+=1
            return temp_count
        for i in range(len(s)):
            odd_count=expand(i,i)
            even_count=expand(i,i+1)

            count+=odd_count+even_count
        
        return count
        