class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nlogk better than nlogn
        # mapp=Counter(nums)
        # stack=[]
        # for key,v in mapp.items():
        #     heapq.heappush(stack,(v,key))
        #     if len(stack)>k:
        #         heapq.heappop(stack)
        # return [key for v,key in stack]

        # mapp=Counter(nums)
        # new =sorted(mapp.items(),key=lambda x:x[1],reverse=True)
        # result=[]
        # for i in range(k):
        #     result.append(new[i][0])
        # return result  

        #BUCKET SORT basically sort on the basis of the frequency
        
        # get the frequencies
        mapp=Counter(nums)
        #form the buckets
        n=len(nums)
        buckets=[[] for i in range(n+1)]
        print(mapp)
        #go throught he mapp for each number and it's frequency add the 
        #same number to their respective bucket size (frequency)
        for key,v in mapp.items():
            buckets[v].append(key)    
        result=[]
        print(buckets)
        #traverse backward of the bucket for most frequencies 
        for b in range(n,-1,-1):
            for key in buckets[b]:
                result.append(key)
                if len(result)==k:
                    return result
        return result    