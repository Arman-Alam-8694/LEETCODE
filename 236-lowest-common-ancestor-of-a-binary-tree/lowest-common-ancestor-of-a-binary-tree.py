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
            if node is None or node==p or node==q:
                return node
            lf=dfs(node.left)
            rf=dfs(node.right)
            if lf and rf:
                return node
            elif not lf:
                return rf
            else:
                return lf
        
        return dfs(root)

        