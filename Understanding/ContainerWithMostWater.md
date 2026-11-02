# Given

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

# Attempt 1

```py
    def maxArea(self, height: list[int]) -> int:
        def get_area(l,r):
            return (r-l) * min(height[l],height[r])

        left = 0
        right = len(height)-1
        maxa=get_area(left,right)

        while left<right:
            lh=height[left]
            rh=height[right]
            if lh <= rh:
                left+=1
            else:
                right-=1

            area = get_area(left,right)
            maxa = max(maxa,area)

        return maxa
```

# Solution

attempt 1 is the solution , surprised i was able to do it alone. Not sure if it's because I saw it along time ago.