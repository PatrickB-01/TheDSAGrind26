class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def printLinkedList(head:ListNode)->None:
    curr =head
    while curr != None:
        print(curr.val)
        curr=curr.next

def buildLinkedListFromArray(arr:list)->ListNode|None:
    if len(arr)==0:
        return None
    head = ListNode(arr[0],None)
    curr = ListNode(None,None)
    for i in range(len(arr)):
        if i==0:
            curr= head
        else:
            curr.next = ListNode(arr[i],None)
            curr= curr.next
    return head
