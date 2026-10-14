class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comb={}

        for str in strs:

            key=''.join(sorted(str))

            if key not in comb:
                comb[key]=[]
            
            comb[key].append(str)

        return list(comb.values())
        