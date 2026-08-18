# Problem

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

## Attempt 1 

Well at this point monotonic stack is most probable, but figuring out the stack invariant is tricky.
i figured that i would need to keep appending to the stack as long as the rectangle is getting larger.
But could not figure out what to do otherwise 

# Solution

```py
# Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        stack = []

        # Nearest Smaller to Left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Nearest Smaller to Right
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
```

## Explanation

**Key Insight:** For each bar, find the maximum width rectangle where that bar is the height. The width extends left and right until we hit a bar that is shorter.

**Algorithm:**

1. **Find Nearest Smaller to Left (NSL):** For each index `i`, find the index of the nearest bar to the left that is smaller than `heights[i]`. If no such bar exists, use `-1`.
   - Use a monotonic stack in increasing order of heights
   - When we encounter a bar shorter than the top of the stack, pop until we find one smaller or the stack is empty
   - The new top (if exists) is the NSL index

2. **Find Nearest Smaller to Right (NSR):** Same concept but scanning right-to-left.
   - This finds the nearest bar to the right that is smaller than `heights[i]`. If none exists, use `n`.

3. **Calculate Maximum Area:** For each bar at index `i`:
   - The maximum width where this bar is the limiting height is: `right[i] - left[i] - 1`
   - Width extends from `left[i] + 1` (first bar taller than NSL) to `right[i] - 1` (last bar before NSR)
   - Area = `heights[i] * width`

**Time Complexity:** O(n) - each element is pushed and popped from the stack exactly once
**Space Complexity:** O(n) - for the stack and two arrays

**Example:** For `heights = [2,1,5,6,2,3]`
- At index 2 (height 5): NSL is at index 1 (height 1), NSR is at index 4 (height 2)
- Width = 4 - 1 - 1 = 2, Area = 5 * 2 = 10