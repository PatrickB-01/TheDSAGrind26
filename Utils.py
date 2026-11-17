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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i]) 
        print(f"Inserting child {arr[ 2 * i + 1] if 2 * i + 1<n else None} for parent {arr[i]}")
        print(f"Inserting child {arr[ 2 * i + 2]  if 2 * i + 2<n else None} for parent {arr[i]}")
        # insert left child 
        
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
        

        # insert right child 
        
        root.right = insertLevelOrder(arr, 2 * i + 2, n)

        
    return root

def preOrderTraversal(node:TreeNode):
    if node is None:
        return
    print(node.val, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node:TreeNode):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.val, end=", ")
    inOrderTraversal(node.right)

def postOrderTraversal(node:TreeNode):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.val, end=", ")

def buildBinaryTreeFromList(arr:list)->TreeNode|None:
    if len(arr)==0:
        return None

    root=  insertLevelOrder(arr,0,len(arr))
    return root

def printTree(root:TreeNode)->None:
    """
    PreOrder Traversal
    """
    # Function to print tree nodes in 
    # PreOrder fashion 

    if root != None:
        print(root.val,end=" ") 
        printTree(root.left) 
        printTree(root.right)
    else: return