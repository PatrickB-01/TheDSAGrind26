

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        window =[0,1]
        windowSize = 1
        maxa = min(height[window[0]],height[window[1]]) * (window[1]-window[0])
        while windowSize <= len(height):
            area = min(height[window[0]],height[window[1]]) * (window[1]-window[0])
            if area > maxa:
                maxa = area
            
            if window[1] != (len(height)-1):
                window[0]+=1
                window[1]+=1
            else:
                windowSize+=1
                window[0]=0
                window[1]= windowSize-1


        return maxa
    
# bad time complexity

    def maxArea2(self, height: List[int]) -> int:
        window =[0,len(height)-1]
        maxa = min(height[window[0]],height[window[1]]) * (window[1]-window[0])
        while window[0] < window[1]:
            area = min(height[window[0]],height[window[1]]) * (window[1]-window[0])
            if area > maxa:
                maxa = area
            
            if height[window[1]] >  height[window[0]]:
                window[0]+=1  
            else:
                window[1]-=1


        return maxa

# better solution
# After area calculation , we want to move one of the pointers. How can we judge it? We want to keep taller height between left and right because there is a possibility that we will get max area with the taller height.

s= Solution()
h =[1,8,6,2,5,4,8,3,7]
r = s.maxArea(h)