class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            Keys="".join(sorted(i))
            if Keys not in dict:
                dict[Keys]=[]
        for i in strs:
            sorted_words="".join(sorted(i))
            for key in dict.keys():
                if sorted_words == key:
                    dict[key].append(i)
        return list(dict.values())