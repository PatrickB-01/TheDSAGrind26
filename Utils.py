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
    if not arr:
        return None

    if arr[0] is None:
        if any(value is not None for value in arr[1:]):
            raise ValueError("A tree cannot have nodes without a root.")
        return None

    root = TreeNode(arr[0])
    parents = [root]
    parent_index = 0
    value_index = 1

    while value_index < len(arr) and parent_index < len(parents):
        parent = parents[parent_index]
        parent_index += 1

        left_value = arr[value_index]
        value_index += 1
        if left_value is not None:
            parent.left = TreeNode(left_value)
            parents.append(parent.left)

        if value_index < len(arr):
            right_value = arr[value_index]
            value_index += 1
            if right_value is not None:
                parent.right = TreeNode(right_value)
                parents.append(parent.right)

    if any(value is not None for value in arr[value_index:]):
        raise ValueError("Input contains nodes with no available parent.")

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