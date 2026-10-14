class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s={}
        set_t={}
        for num in s:
            if num in set_s:
                continue
            count_num=s.count(num)
            set_s[num]=count_num
        for num in t:
            count_num=t.count(num)
            set_t[num]=count_num
        if set_s==set_t:
            return(True)
        else:
            return(False)
        