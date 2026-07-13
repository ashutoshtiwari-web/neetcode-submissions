class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        count=0 
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        sorted_dt=dict(sorted(hashmap.items(),key=lambda item:item[1],reverse=True))
        final=list(sorted_dt.keys())[:k]
        return final
    