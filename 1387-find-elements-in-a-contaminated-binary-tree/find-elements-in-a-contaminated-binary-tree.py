# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.findelements=set()
        self.populatelist(root,0)

    def populatelist(self,node,val):
        self.findelements.add(val)
        if node.left:
            new_val=val*2+1

            self.populatelist(node.left,new_val)
        if node.right:
            new_val=val*2+2
            self.populatelist(node.right,new_val)

        

    def find(self, target: int) -> bool:
        if target in self.findelements:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)