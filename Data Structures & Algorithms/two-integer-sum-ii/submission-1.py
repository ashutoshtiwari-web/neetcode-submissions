class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index=1
        for j in range(len(numbers)):
            for i in range(start_index,len(numbers)):
                if numbers[j]+numbers[i]==target:
                    index=[j+1,i+1]
                    return index
                
            start_index+=1