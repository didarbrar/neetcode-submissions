class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comb={}
        my_dict={
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
        }
        for str in strs:
            key=[0]*26
            for s in str:
                key[my_dict[s]]+=1
            
            #key=''.join(sorted(str))

            if tuple(key) not in comb:
                comb[tuple(key)]=[]
            
            comb[tuple(key)].append(str)

        return(list(comb.values()))
        