class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            dist = {}
            steps = 0
            while start != -1 and start not in dist:
                dist[start] = steps
                steps += 1
                start = edges[start]
            return dist
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        result = float('inf')
        answer = -1
        if len(dist1)<=len(dist2):
            first=dist1
            second=dist2
        else:
            first=dist2
            second=dist1        
        for node in first.keys():
            if node in second:
                max_dist = max(first[node], second[node])
                if max_dist < result or (max_dist == result and node < answer):
                    result = max_dist
                    answer = node
                    
        return answer
