# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.answer=None
        # self.p_find=False
        # self.q_find=False
        # def dfs(root,p,q):
        #     tp_find,tq_find=False,False
        #     if not root:
        #         return False,False
        #     if root==p:
        #         self.p_find=True
        #         tp_find=True
        #     if root==q:
        #         tq_find=True
        #         self.q_find=True
            
        #     if self.p_find and self.q_find:
        #         return tp_find,tq_find
        #     p1,q1=dfs(root.left,p,q)
        #     p2,q2=dfs(root.right,p,q)
        #     if tp_find:
        #         if q1 or q2:
        #             self.answer=p
        #     elif tq_find:
        #         if p1 or p2:
        #             self.answer=q
        #     else:
        #         if (p1 or p2) and (q1 or q2):
        #             if not self.answer:
        #                 self.answer=root  
        #     return (p1 or p2 or tp_find),(q1 or q2 or tq_find)
        # dfs(root,p,q)
        # return self.answer



        #simplified
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        self.answer=False
        
        def dfs(node):
            if not node:
                return False, False
            
            left_p_found, left_q_found = dfs(node.left)
            right_p_found, right_q_found = dfs(node.right)
            
            # Check if the current node is either p or q
            current_p = (node == p)
            current_q = (node == q)
            
            # p and q found in left or right subtree or at the current node
            p_found = left_p_found or right_p_found or current_p
            q_found = left_q_found or right_q_found or current_q
            
            # If current node is the LCA
            if p_found and q_found and not self.answer:
                self.answer = node
            
            return p_found, q_found
        
        dfs(root)
        return self.answer

        