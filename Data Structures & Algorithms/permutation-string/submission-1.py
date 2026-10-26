class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq_s1={}
        for ch in s1:

            freq_s1[ch]=freq_s1.get(ch,0)+1
        for r in range(len(s2)-len(s1)+1):
            sub_string=s2[r:r+len(s1)]
            freq_s2={}
            for ch in sub_string:
                freq_s2[ch]=freq_s2.get(ch,0)+1
            
            if freq_s1==freq_s2:
                return True
        return False
            
