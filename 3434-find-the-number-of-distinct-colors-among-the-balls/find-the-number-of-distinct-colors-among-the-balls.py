class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mapp={}
        colors=defaultdict(int)
        n=len(queries)
        result=[]
        distinct=0
        for i in range(n):
            ball_no,color=queries[i]
            if ball_no in mapp:
                prev_color=mapp[ball_no]
                colors[prev_color]-=1
                if colors[prev_color]==0:
                    del colors[prev_color]
                    distinct-=1
                if color not in colors:
                    distinct+=1
                mapp[ball_no]=color
            else:
                if color not in colors:
                    distinct+=1
                mapp[ball_no]=color

            colors[color]+=1
            result.append(distinct)
        return result
            



        