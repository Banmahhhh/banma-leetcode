'''
Use stack, push right, itself, left, then pop
after pushing, remove the connection fron the node and children
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        tree_stack = []
        tree_stack.append(root)
        answer = []
        temp = root
        while(len(tree_stack)): #TODO
            temp = tree_stack.pop()
            if temp.right == None and temp.left == None:
                answer.append(temp.val)
            else:
                if temp.right != None:
                    tree_stack.append(temp.right)
                    temp.right = None           
                tree_stack.append(temp)
                if temp.left != None:
                    tree_stack.append(temp.left)
                    temp.left = None
                
            
