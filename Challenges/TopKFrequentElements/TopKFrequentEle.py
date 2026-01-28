"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


import heapq
from itertools import count
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #failed
        counts={}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        
        top = [(0,0)]*k
        for key,v in counts.items():
            for i in range(len(top)):
                if v > top[i][1]:
                    top[i]=(key,v)
        topr = []
        for key,v in top:
            topr.append(key)
        return topr
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        #Works but needs improvement
        setu = set(nums)
        counts={}
        for n in setu:
            counts[n]=nums.count(n)
        top = sorted(counts.items(), key=lambda kv:kv[1],reverse=True)
        return [t[0] for t in top[:k]]
    
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        # works but same performace as 2
        counts={}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        top = [(0,0)]*k
        for key,v in counts.items():
            for i in range(k):
                if v > top[i][1]:
                    top.insert(i,(key,v))
                    top.pop()
                    break
        return [t[0] for t in top]
    
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        # Works a bit better than the previous
        counts={}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        counter = count()
        heap = []
        for key,v in counts.items():
            heapq.heappush(heap,(v,key))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [t[1] for t in heap]
    
    def topKFrequent5(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        counts={}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        freq = [[] for _ in range(len(nums)+1)]

        for key,v in counts.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            if len(freq[i])>0:
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        
        return res
        
    
    
    
    


nums = [1,2,1,2,1,2,3,1,3,2]
k=2
s=Solution()
r= s.topKFrequent5(nums=nums,k=k)
print(r)