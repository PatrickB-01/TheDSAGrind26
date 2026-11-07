# Given

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Constraints:

1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
1 <= k <= nums.length

# Attempt 1 

no idea tried for a bit

```py
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    left =0
    right=k-1
    maxes=[]
    index_max = max(range(k), key=nums[left:right+1].__getitem__)
    max_cw = nums[right-k+1+index_max]
    maxes.append(max_cw)

    

    while right < len(nums)-1:
        left+=1
        right+=1
        if index_max <left:
            index_max = max(range(k), key=nums[left:right+1].__getitem__)
            max_cw = nums[right-k+1+index_max]
        else:
            max_cw= max(nums[left],nums[right],max_cw)
        maxes.append(max_cw)

    return maxes
```


# Solution

```py
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for idx, num in enumerate(nums):
            # Maintain the deque in descending order
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            # Remove the elements which are out of this window
            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            # Append the maximum of the current window to the result
            if idx >= k - 1:
                res.append(q[0])
        
        return res
```