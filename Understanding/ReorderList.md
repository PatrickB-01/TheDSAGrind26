# Given

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000


# Attempt 1

```py
def reorderList(head: ListNode | None) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head.next == None:
        return
    nodes =[]
    curr=head
    while curr!=None:
        nodes.append(curr)
        curr = curr.next

    curr = head
    left=1
    right=len(nodes)-1
    for i in range(len(nodes)):
        if i==0:
            continue

        if i%2==0:
            # even
            curr.next = nodes[left]
            curr = curr.next
            left+=1
        else:
            #odd
            curr.next = nodes[right]
            curr = curr.next
            right-=1

        curr.next=None
```

Solved but had to use extra space with O(n) time complexity, maybe there is a better way
There us a better way
if we combine the 2 pointer slow fast we can know the middle  of the list
then if we reverse the second half
and finally apply the merge to the first half and the reversed second half alternatively then

# Solution

```py
def reorderList(head: ListNode | None) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head.next == None:
        return
    curr=head

    # find mid
    slow= head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow= slow.next

    # Reverse the second half
    curr = slow.next
    if curr ==None:
        return
    next_n= curr.next
    revh = slow.next
    revh.next=None
    while next_n!=None:
        curr=next_n
        next_n= curr.next
        curr.next = revh
        revh =curr

    #Utils.printLinkedList(revh)
    slow.next = None
    #Utils.printLinkedList(head)

    # Merge
    c=True
    curr1=head
    curr2= revh
    while curr1 and curr2:
        if c:
            # put from rev
            next_1 = curr1.next
            curr1.next = curr2
            curr1 = next_1
            c=not c
        else:
            # put from normal
            next_2= curr2.next
            curr2.next = curr1
            curr2= next_2
            c=not c

```

By using a 3 step approach we can solve it without using extra space
slow fast to find the mid
once mid is found reverse the second part
once reversed merge the 2 halves