# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp={}
        for i in range(len(preorder)):
            mapp[inorder[i]]=i
        
        def buildtree(prestart,preend,instart,inend,mapp):
            if prestart>preend or instart>inend:
                return None
            node=TreeNode(preorder[prestart])
            idx=mapp[preorder[prestart]]
            count=idx-instart
            node.left=buildtree(prestart+1,prestart+count,instart,idx-1,mapp)
            node.right=buildtree(prestart+count+1,preend,idx+1,inend,mapp)
            return node






        return buildtree(0,len(preorder)-1,0,len(inorder)-1,mapp)





                
        