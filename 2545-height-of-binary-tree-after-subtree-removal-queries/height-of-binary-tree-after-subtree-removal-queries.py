from collections import defaultdict
import heapq
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level_depths = defaultdict(list)  # Store all depths for each level
        node_levels = {}  # Store level for each node
        max_depth_from_root = {}  # Store max depth for each node's subtree
        
        def dfs(node, level, depth):
            if not node:
                return depth - 1
            
            node_levels[node.val] = level
            
            left_depth = dfs(node.left, level + 1, depth + 1)
            right_depth = dfs(node.right, level + 1, depth + 1)
            
            max_depth = max(left_depth, right_depth)
            max_depth_from_root[node.val] = max_depth
            
            # Store all depths at each level
            level_depths[level].append((-max_depth, node.val))
            
            return max_depth
            
        dfs(root, 0, 0)
        
        # Sort depths at each level
        for level in level_depths:
            level_depths[level].sort()
            
        answer = []
        for query in queries:
            level = node_levels[query]
            depths = level_depths[level]
            
            # If only one node at this level
            if len(depths) == 1:
                answer.append(level - 1)
                continue
                
            # If queried node is not the highest depth node
            if depths[0][1] != query:
                answer.append(-depths[0][0])
                continue
                
            # If queried node is the highest depth node, use second highest
            answer.append(-depths[1][0])
            
        return answer