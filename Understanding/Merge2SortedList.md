# Given

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

# Attempt 1

```py
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    curr1 = list1
    curr2 = list2
    if list1==None and list2 ==None:
        return None
    if list1 == None and list2 !=None:
        return list2
    if list1 != None and list2 ==None:
        return list1
    
    while curr1!=None and curr2!=None:

        if curr1.val >= curr2.val:
            if curr2.next==None or curr1.val <=curr2.next.val:
                next1 = curr1.next
                next2 = curr2.next
                curr2.next= curr1
                curr1.next=next2
                curr1=next1
                curr2 = curr2.next
            elif curr1.val >curr2.next.val :
                curr2=curr2.next
        elif curr1.val <= curr2.val:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next=curr2
            if curr2 == list2:
                list2 =curr1
            curr2 =curr1
            curr1=next1


    return list2
```
Worked but had to solve edge cases alot
there should be a better way i think

# Solution

```py
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next
```