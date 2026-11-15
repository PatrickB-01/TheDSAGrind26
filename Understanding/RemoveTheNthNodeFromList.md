# Given

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?


# Attempt 1

```py

    slow=head
    fast=head
    if head.next==None:
        return None
    
    for _ in range(n-1):
        fast=fast.next

    if fast.next==None:
        if slow== head:
            head=head.next
        else:
            nnext = slow.next.next
            slow.next= nnext

    while fast.next:
        fast= fast.next
        if fast.next != None:
            slow=slow.next
        else:
            # if slow== head:
            #     head=head.next
            # else:
            nnext = slow.next.next
            slow.next= nnext
    return head
```
attempt 1 was the solution, the trick here is using 2 pointers that move at constant pace/speed but start at a "n" distance apart so that the even after they move the distance between them is always "n"

# Solution

