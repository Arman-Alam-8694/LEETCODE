from collections import defaultdict
from typing import List, Optional

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level_depths = defaultdict(lambda: [(-1, -1), (-1,-1)])  # Initialize with -1 depths
        node_levels = {}  # Store level for each node
        
        def dfs(node, level, depth):
            if not node:
                return depth - 1
            
            node_levels[node.val] = level
            
            left_depth = dfs(node.left, level + 1, depth + 1)
            right_depth = dfs(node.right, level + 1, depth + 1)
            
            max_depth = max(left_depth, right_depth)
            
            # Update top 2 depths for this level
            curr_max, second_max = level_depths[level]
            if max_depth > curr_max[0]:
                level_depths[level] = [(max_depth, node.val), curr_max]
            elif max_depth > second_max[0]:
                level_depths[level] = [curr_max, (max_depth, node.val)]
            
            return max_depth
            
        dfs(root, 0, 0)
        
        answer = []
        for query in queries:
            level = node_levels[query]
            first, second = level_depths[level]
            
            # If query node has max depth, use second max
            if first[1] == query:
                # If no second max exists (single node at level), use level-1
                if second[0] == -1:
                    answer.append(level - 1)
                else:
                    answer.append(second[0])
            # Otherwise use first max
            else:
                answer.append(first[0])
            
        return answer