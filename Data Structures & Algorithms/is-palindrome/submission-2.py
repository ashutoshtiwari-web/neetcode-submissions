class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=[]
        for i in range(0,len(s)):    
            if s[i].isalnum():
                ch.append(s[i].lower())
        if ch==ch[::-1]:
            return True        
        return False


        