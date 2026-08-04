# Problem

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Attempt 1

```py
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count={}
    for n in nums:
        if n in count:
            count[n]+=1
        else:
            count[n] = 1
    maxes=set()
    while len(maxes) < k:
        maxi=[0,0]
        for key,v in count.items():
            if v > maxi[1] and key not in maxes:
                maxi=[key,v]
        maxes.add(maxi[0])
    return list(maxes)
```

In my first attemp i counted then i looped while until i found the most k frequent elements
O(n)



# Solution


The solution to achieve O(nlogn) would be to use a heap (max heap), because a heap keeps the max or min at the top so that when you pop you will get the current min or max in the heap. So that way you have fast access to the max or min

```py
def topKFrequent(nums: list[int], k: int) -> list[int]:
    import heapq
    count={}
    for n in nums:
        if n in count:
            count[n]+=1
        else:
            count[n] = 1
    heap = []
    for key,v in count.items():
        heapq.heappush(heap,(-v,key))
    res =[]
    while len(res) < k:
        nv,key = heapq.heappop(heap)
        res.append(key)
    return res
```