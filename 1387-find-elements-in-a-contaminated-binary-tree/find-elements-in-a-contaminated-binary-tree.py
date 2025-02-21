

class FindElements:
    #memory efficient code but time complexity O(N*logN)
    # def __init__(self, root: TreeNode):
    #     self.root = root

    # def getPath(self, target: int) -> str:
    #     path=[]
    #     while target>0:
    #         path.append("L" if target%2 else "R")
    #         target=(target-1)//2 if target%2 else (target-2)//2
    #     return reversed(path)


    # def find(self, target: int) -> bool:
    #     path=self.getPath(target)
    #     node=self.root
    #     for i in path:
    #         if i=="L" and node.left:
    #             node=node.left
    #         elif i=="R" and node.right:
    #             node=node.right
    #         else:
    #             return False

    #     return True

    #faster and simpler to think appraoch with time complexity of O(N)

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
       
# Usage:
# obj = FindElements(root)
# param_1 = obj.find(target)
