class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=0
        p_list=[]
        
        while l<len(nums):
            product=1
            for i in range(len(nums)):
                if i!=l:
                    product=product*nums[i]
                
            p_list.append(product)    
            l+=1
        return p_list