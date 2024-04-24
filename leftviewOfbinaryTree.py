class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
def leftViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    
    print(*result)

root=TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(3)
obj5 = TreeNode(9)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10 = TreeNode(12)
obj11 = TreeNode(14)
obj12 = TreeNode(20)
obj13 = TreeNode(18)
obj14 = TreeNode(25)

root.left = obj2 
root.right = obj8 
 
obj2.left = obj3 
obj2.right = obj5 
 
obj3.left = obj4 

obj2.left = obj3 
obj2.right = obj5 
 
obj5.left = obj6 
obj5.right = obj7 
 
obj8.left = obj9 
obj8.right = obj12 
 
obj9.left = obj10
obj9.right = obj11


obj12.left = obj13 
obj12.right = obj14
leftViewOfBinaryTree(root)



Write a program to find right view of a binary tree by constructing a binary-tree. Construct binary-tree for below image.

https://imgs.search.brave.com/pmXepTjoef7x4-rfkVoUdmoXjDfTg-tEkhMlTnM1u9c/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9yZXMu/Y2xvdWRpbmFyeS5j/b20vcHJhY3RpY2Fs/ZGV2L2ltYWdlL2Zl/dGNoL3MtLWxUT3I5/UDRGLS0vY19saW1p/dCxmX2F1dG8sZmxf/cHJvZ3Jlc3NpdmUs/cV9hdXRvLHdfODgw/L2h0dHBzOi8vZGV2/LXRvLXVwbG9hZHMu/czMuYW1hem9uYXdz/LmNvbS9pL2hvcjZy/Mm9rNWZzaGdneDFh/cGQ2LnBuZw



Sample Output 0

11 15 20 25
