"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from collections import defaultdict
from typing import List
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        entries = defaultdict(list)
        for i in nums:
            entries[i].append(i)
            if (i+1) in entries:
                entries[i+1].append(i)
            if (i-1) in entries:
                entries[i-1].append(i)
        
        seq= defaultdict(set)

        for k,v in entries.items():
            if k not in seq:
                seq[k]= set(v)
            else:
                pass

        return 0

# solution
    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0

        for n in nums:
            if n-1 not in nums:
                length = 1
                while n + length in nums:
                    length+=1
                longest = max(longest,length)
        return longest

s= Solution()
nums=[100,4,200,1,3,2]
s.longestConsecutive2(nums)