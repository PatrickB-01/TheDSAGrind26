# Given
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.


# Attempt 1

```py
def hasCycle(head: Optional[ListNode]) -> bool:
    if head == None or head.next==None:
        return False
    
    p1=head
    p2=head.next
    seen = set()
    c=0
    while p1 != None:
        if p1 in seen:
            return True
        else:
            seen.add(p1)
            p1=p1.next



    return False
```

this is at the expense of space but i know there isa way to do it using 2 pointers with one moving faster to catchup and do 1 lap

# Attempt 2

```py
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next==None:
            return False
        p1=head
        p2=head
        c=0
        while p2 != None:
            if c<2:
                p2=p2.next
                c+=1
            else:
                p1=p1.next
                c=0
            if p1 == p2:
                return True
        return False
```
better O(1) space

# Attempt 3

```py
def hasCycle(head: ListNode|None) -> bool:
    if head == None or head.next==None:
        return False
    p1=head
    p2=head
    while p2 != None:
        p2=p2.next
        if p2 != None:
            p2=p2.next
        p1=p1.next

        if p1 == p2:
            return True
    return False
```

# Solution

attempts 2 and 3 are the solutions , by having 2 pointers and one moving faster than the other eventually if there is a cycle they will meet