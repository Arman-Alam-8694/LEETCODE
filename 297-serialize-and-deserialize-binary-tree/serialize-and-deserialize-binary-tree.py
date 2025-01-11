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
        idx=0
        print(data)
        def dfs(idx):
            
            if idx>len(data):
                return idx
            num=data[idx]
            if num=="N":
                return None,idx
            Node=TreeNode(num)
            idx+=1
            Node.left,idx=(dfs(idx))
            idx+=1
            Node.right,idx=(dfs(idx))
            return Node,idx
        return dfs(0)[0]
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))