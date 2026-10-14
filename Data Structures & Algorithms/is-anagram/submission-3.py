class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        set_s={}
        set_t={}
        for num in s:
            if num in set_s:
                continue
            count_num=s.count(num)
            set_s[num]=count_num
        for num in t:
            if num in set_t:
                continue
            count_num=t.count(num)
            set_t[num]=count_num
        if set_s==set_t:
            return(True)
        else:
            return(False)
        