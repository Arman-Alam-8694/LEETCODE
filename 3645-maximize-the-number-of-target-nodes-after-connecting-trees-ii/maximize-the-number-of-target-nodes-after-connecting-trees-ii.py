from collections import defaultdict, deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_tree(edges):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree

        def color_tree(tree, n):
            color = {}
            queue = deque([(0, 'red')])
            red_count = 0
            blue_count = 0
            while queue:
                node, c = queue.popleft()
                if node in color:
                    continue
                color[node] = c
                if c == 'red':
                    red_count += 1
                else:
                    blue_count += 1
                for nei in tree[node]:
                    if nei not in color:
                        queue.append((nei, 'blue' if c == 'red' else 'red'))
            return color, red_count, blue_count

        n = len(edges1) + 1
        m = len(edges2) + 1

        tree1 = build_tree(edges1)
        tree2 = build_tree(edges2)

        # Color both trees
        color1, red1, blue1 = color_tree(tree1, n)
        color2, red2, blue2 = color_tree(tree2, m)

        # For each node in tree1, calculate maximum target nodes
        result = []
        for i in range(n):
            my_color = color1[i]
            same_color_count = red1 if my_color == 'red' else blue1
            max_other = max(red2, blue2)
            result.append(same_color_count + max_other)

        return result
