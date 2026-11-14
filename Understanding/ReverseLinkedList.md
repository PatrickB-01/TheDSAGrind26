# Given

Given the head of a singly linked list, reverse the list, and return the reversed list.

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

# Attempt 1

```py
def reverseList(head: ListNode | None) -> ListNode | None:
    if head ==None:
        return head
    next_n=head.next
    curr= head
    revh = head 
    revh.next=None
    while next_n != None:
        curr = next_n
        next_n= curr.next
        curr.next = revh
        revh =curr
    return revh
```

# solution

Attempt 1 was the solution