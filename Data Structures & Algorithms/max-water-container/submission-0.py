class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        start=0
        t=0
        while t<len(heights)-1:
            for i in range(t+1,len(heights)):
                if heights[t]>=heights[i] and (heights[i]*(i-t))>max_area:
                    max_area=heights[i]*(i-t)
                elif heights[i]>=heights[t] and (heights[t]*(i-t))>max_area:
                    max_area=heights[t]*(i-t)
            t+=1    

        return max_area