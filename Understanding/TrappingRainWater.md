# Given

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

# Attempt 1

```py
def trap(height: list[int]) -> int: 
    left=0
    right=len(height)-1
    hl=height[left]
    hr=height[right]
    level=min(hl,hr)
    water = (right-left) * level

    while left<right:
        
        hl=height[left]
        hr=height[right]
        current_level = min(hl,hr)

        if hl<=hr:
            left+=1
            hl=height[left]
            hr=height[right]
            current_level = min(hl,hr)
            if  hl>0:
                if hl<=level:
                    water-=hl
                else:
                    water-=level
            
            if current_level > level:
                water += (right-left) * (current_level-level)
                level = current_level
            
        else:
            right-=1
            hl=height[left]
            hr=height[right]
            current_level = min(hl,hr)
            if  hr>0:
                if hr<=level:
                    water-=hr
                else:
                    water-=level

            if current_level > level:
                water += (right-left) * (current_level-level)
                level = current_level

    return water

```


# Solution

Was able to solve it from the first attempt but took more than 30 minm the additional time was spent on figuring out when to update the level
