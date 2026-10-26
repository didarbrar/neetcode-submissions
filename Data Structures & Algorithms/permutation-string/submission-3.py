class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)

        if m>n:
            return False
        freq_s1={}
        freq_s2={}

        for i in range(m):
            freq_s1[s1[i]]=freq_s1.get(s1[i],0)+1
            freq_s2[s2[i]]=freq_s2.get(s2[i],0)+1
        
        if freq_s1==freq_s2:
            return True
        
        for r in range(m,n):
            incoming=s2[r]
            outgoing=s2[r-m]

            freq_s2[incoming]=freq_s2.get(incoming,0)+1
            freq_s2[outgoing]-=1

            if freq_s2[outgoing]==0:
               del freq_s2[outgoing]
            
            if freq_s1==freq_s2:
                return True
        return False