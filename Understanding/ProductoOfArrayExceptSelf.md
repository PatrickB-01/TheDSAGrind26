# Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Attempt 1

i honestly had no clue what i was doing, but started with a up and down approach where i multiply current and previous element and store in an array

# Solution

So it seems i had the correct direction i had to get the prefix and suffix product arrays
But the trick here is to 
```
pre[i] = pre[i - 1] * a[i - 1]
suff[i] = suff[i + 1] * a[i + 1]
result[i] = pre[i] * suff[i]
```
```py
def productExceptSelf(nums: list[int]) -> list[int]:
    pre=[None]*len(nums)
    suff=[None]*len(nums)
    result=[]
    pre[0]=1
    suff[len(nums)-1]=1

    #pre
    for i in range(1,len(nums)):
        pre[i]= pre[i-1] * nums[i-1]

    for i in range(len(nums)):
        rear_idx= len(nums)-1-1
        suff[rear_idx] = suff[rear_idx +1] * nums[rear_idx+1]

    for i in range(len(nums)):
        result[i] = pre[i] * suff[i]

    return result
```

for the follow up to reduce space i could have used the result array to store the prefix and suffix

```py
def productExceptSelf(nums: list[int]) -> list[int]:

    result=[1]*len(nums)
    #pre
    curr=1
    for i in range(1,len(nums)):
        result[i] *= curr
        curr = nums[i]

    # suff    
    curr=1
    for i in range(len(nums)):
        rear_idx= len(nums)-1
        result[rear_idx] *= curr
        curr = nums[rear_idx]

    return result
```