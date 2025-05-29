from collections import defaultdict, deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        treeone = defaultdict(list)
        treetwo = defaultdict(list)
        nodeclr = defaultdict(str)

        # Build both trees and track all nodes
        for s, e in edges1:
            treeone[s].append(e)
            treeone[e].append(s)
        for s, e in edges2:
            treetwo[s].append(e)
            treetwo[e].append(s)

        def colour(start, tree, save_color=False):
            queue = deque([(start, "red")])
            seen = set()
            redcnt = 0
            bluecnt = 0
            while queue:
                node, prevcolor = queue.popleft()
                if node in seen:
                    continue
                seen.add(node)

                # Count colors
                if prevcolor == "red":
                    redcnt += 1
                else:
                    bluecnt += 1
                # Save color mapping if needed
                if save_color:
                    nodeclr[node] = prevcolor

                # Enqueue unvisited neighbors
                for child in tree[node]:
                    if child not in seen:
                        queue.append((child, "blue" if prevcolor == "red" else "red"))
            return redcnt, bluecnt

        # Color treeone and record each node's color
        r, b = colour(0, treeone, save_color=True)
        fast = {"red": r, "blue": b}

        # Color treetwo just to get its max color group
        sred, sblue = colour(0, treetwo)
        smax = max(sred, sblue)

        # Number of nodes in treeone is len(edges1) + 1
        n = max(treeone.keys())+1
        result = []
        # Build result for each node 0..n-1
        for i in range(n):
            result.append(fast[nodeclr[i]] + smax)

        return result
