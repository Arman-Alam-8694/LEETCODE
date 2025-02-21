

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root

    def getPath(self, target: int) -> str:
        path = []
        while target != 0:
            if target % 2:
                path.append('L')
                target = (target - 1) // 2
            else:
                path.append('R')
                target = (target - 2) // 2
        return ''.join(reversed(path))

    def find(self, target: int) -> bool:
        path = self.getPath(target)
        cur_node = self.root

        for direction in path:
            if direction == 'L' and cur_node.left:
                cur_node = cur_node.left
            elif direction == 'R' and cur_node.right:
                cur_node = cur_node.right
            else:
                return False
        return True

# Usage:
# obj = FindElements(root)
# param_1 = obj.find(target)
