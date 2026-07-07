class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        si=0
        for si in range(len(nums)):
            for i in range(si+1,len(nums)):
                if nums[si]+nums[i]==target:
                    return [si,i]     
                
      
            