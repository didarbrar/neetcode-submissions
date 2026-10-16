class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        n=len(s)
        left=0
        right=n-1
        palon=True
        while left<=right:
            if s[left]==" ":
                left+=1
            elif s[right]==" ":
                right-=1
            elif s[left]==s[right]:
                left+=1
                right-=1
            else:
                palon=False
                break
        return palon   
        