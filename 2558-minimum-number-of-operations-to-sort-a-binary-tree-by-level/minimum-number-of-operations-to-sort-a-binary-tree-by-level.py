# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swaps = 0
        nodes = [root]
        while nodes:
            next_nodes = []
            pos, el, heap = {}, {}, []
            for idx, node in enumerate(nodes):
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                pos[idx] = node.val
                el[node.val] = idx
                heapq.heappush(heap, node.val) 
            for i in range(len(heap)):
                curr = heapq.heappop(heap)
                if pos[i] == curr:
                    continue
                swap = pos[i]
                idx = el[curr]
                pos[idx] = swap
                el[swap] = idx
                swaps += 1
            nodes = next_nodes
        return swaps            
        