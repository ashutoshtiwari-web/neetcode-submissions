class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=0
        if len(list(s))==len(list(t)):
            s_list = list(s)
            t_list = list(t)
            for i in s_list:
                if i in t_list:
                    m+=1
                    t_list.remove(i)
                else:
                    continue
            if m==len(s):
                return True
        return False

