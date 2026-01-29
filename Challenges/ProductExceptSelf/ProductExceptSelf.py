"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from math import prod
from typing import List
class Solution:
    # exceeds time limit
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer =[]
        for i in range(len(nums)):
            answer.append(1)
            for ii in range(len(nums)):
                answer[i] = (answer[i] * nums[ii] ) if ii!=i else answer[i]
        return answer
    # exceeds time limit
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        answer =[]
        for i in range(len(nums)):
            sub:List = nums[:i]
            sub.extend(nums[i+1:])
            answer.append(prod(sub))
        return answer
    
    # best o(n) time and o(1) space excluding answer list
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]

        curr=1
        for i in range(len(nums)):
            answer[i] = answer[i] * curr
            curr = curr * nums[i]

        curr=1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * curr
            curr = curr * nums[i]

        return answer
    
s =Solution()
nums = [1,2,3,4]
s.productExceptSelf3(nums)