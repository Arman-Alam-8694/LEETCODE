# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        stringg=[]
        def dfs(root):
            if not root:
                stringg.append("N")
                return None
            stringg.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res=",".join(stringg)
        return res

    def deserialize(self, data):
        data=data.split(",")
        self.idx=0
        def dfs():
            
            if self.idx>len(data):
                return None
            num=data[self.idx]
            if num=="N":
                return None
            Node=TreeNode(num)
            self.idx+=1
            Node.left=dfs()
            self.idx+=1
            Node.right=dfs()
            return Node
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))