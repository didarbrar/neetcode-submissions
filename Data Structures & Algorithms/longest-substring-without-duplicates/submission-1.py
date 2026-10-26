class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string=set()
        l=0
        r=0
        result=0
        while r<(len(s)):
            ch=s[r]
            if ch not in sub_string:
                sub_string.add(ch)
                result=max(result,r-l+1)
                r+=1
            else:
                sub_string.remove(s[l])
                l+=1
        return result