# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        def buildtree(poststart,postend,instart,inend):
            if poststart<postend or instart>inend:
                return None
            n=postorder[poststart]
            Node=TreeNode(n)
            idx=mapp[n]
            righttree=inend-idx
            Node.right=buildtree(poststart-1,poststart-righttree,idx+1,inend)
            Node.left=buildtree(poststart-righttree-1,postend,instart,idx-1)
            return Node



        return buildtree(len(postorder)-1,0,0,len(inorder)-1)
