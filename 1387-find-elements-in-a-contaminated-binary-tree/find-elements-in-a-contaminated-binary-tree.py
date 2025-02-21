

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root

    def getPath(self, target: int) -> str:
        path=[]
        while target>0:
            path.append("L" if target%2 else "R")
            target=(target-1)//2 if target%2 else (target-2)//2
        return reversed(path)

        # reverse_array=[]
        # for i in range(-1,(-1*len(path))-1,-1):
        #     reverse_array.append(path[i])
        # return reverse_array
        # return "".join(reversed(path))
        # return "".join(reverse_array))
      

    def find(self, target: int) -> bool:
        path=self.getPath(target)
        node=self.root
        for i in path:
            if i=="L" and node.left:
                node=node.left
            elif i=="R" and node.right:
                node=node.right
            else:
                return False

        return True
       
# Usage:
# obj = FindElements(root)
# param_1 = obj.find(target)
