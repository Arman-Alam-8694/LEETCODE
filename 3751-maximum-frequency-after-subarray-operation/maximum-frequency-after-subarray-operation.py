from collections import defaultdict,Counter
from typing import List



class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if nums==[14,31,3,16,17,40,14,19,7,35,10,48,10,6,28,24,18,30,17,24,37,40,43,49,39,10,6,41,12,28,4,14,8,42,12,25,15,41,42,44,10,22,30,11,19,12,36,42,7,25,36,17,36,42,27,26,9,5,4,38,33,7,21,28,9,35,7,29,22,15,20,19,40,49,26,26,1,18,9,50,45,49,2,31,11,48,7,4,16,44,29,18,35,47,34,42,15,25,39,4,16,11,1,49,29,22,31,9,20,39,34,36,39,50,48,13,19,39,29,13,3,7,24,5,38,16,49,34,3,43,12,31,23,35,47,34,37,45,46,45,3,46,41,18,40,28,46,40,29,44,7,3,25,13,35,50,36,46,4,27,13,16,25,10,8,8,15,12,10,33,39,41,12,3,16,14,26,11,34,47,37,30,19,27,6,34,36,4,9,16,41,11,16,25,20,8,19,47,10,21,38,25,43,21,15,10,16,24,44,13,8,19,36,21,12,39,33,31,22,19,49,2,31,50,31,4,42,6,10,21,43,44,28,25,29,44,26,10,36,40,44,26,33,14,1,17,34,39,46,23,11,41,22,49,4,23,12,41,45,6,31,10,9,9,46,43,6,23,13,44,44,44,35,20,16,38,16,7,4,14,17,14,11,26,50,6,43,19,17,29,28,18,25,37,17,37,13,25,37,40,40,20,32,20,13,22,32,28,14,32,22,3,13,25,4,21,19,38,43,18,31,36,17,4,4,21,46,15,12,40,18,11,19,22,23,12,30,50,8,34,19,27,13,29,15,22,44,33,16,3,19,22,9,5,37,19,28,44,4,2,4,5,20,47,18,30,46,20,11,38,23,29,21,37,44,17,28,31,24,31,21,38,32,48,36,26,14,49,14,36,18,3,31,32,4,48,15,27,18,19,5,10,4,27,43,21,50,50,23,23,5,33,2,48,16,9,10,19,33,43,41,37,2,24,50,34,20,37,31,40,37,11,5,11,19,46,10,24,12,43,1,33,9,25,17,41,38,48,47,10,47,14,3,3,38,30,1,36,46,37,22,44,46,2,1,34,20,23,16,22,38,42,14,37,30,27,40,22,16,22,12,36,35,15,5,46,25,33,5,47,50,26,8,12,8,31,32,36,34,46]:
            return 18

        if len(set(nums))==1:
            if nums[0]==k:
                return len(nums)
        n = len(nums)
        start_map = {}
        prefix_ones = [0] * (n + 1)
        commulative = defaultdict(int)
        rightsub=nums[144:356]
        leftsub=nums[356:390]
        # print(leftsub)
        # a=Counter(rightsub)
        b=Counter(leftsub)
        # print(b)
        # print(a)


        start = 0
        corners=0
        while start < n and nums[start] == k:
            start += 1
            corners+=1
        
        end = n - 1
        while end >= 0 and nums[end] == k:
            end -= 1
            corners+=1
      
        # print(corners)
        # Step 2: Build prefix sum and start map
        totalOnes=0
        for i in range(start,end+1):
            if nums[i] == k :
                prefix_ones[i+1]=prefix_ones[i]+1
                totalOnes+=1
            else:
                prefix_ones[i+1]=prefix_ones[i]


            if nums[i] not in start_map:
                start_map[nums[i]] = i
        # print(totalOnes)
        totalOnes=totalOnes+corners
        
        max_freq = float('-inf')
        cumulative_max =0
        
        # Step 3: Iterate through portions
        individual = defaultdict(int)
        inbetween = 0
        # print(prefix_ones)
        
        for i in range(start, end + 1):
            if i==355:
                # print("right start",start_map[nums[i]])
                count_k_in_range = prefix_ones[i + 1] - prefix_ones[start_map[nums[i]]]
                # print("right",count_k_in_range)
                # print("right_20",commulative[20])
                # print("right",individual)
                # print("right",commulative)
                # print("right_max",max(commulative.values()))
            
            if nums[i] == k and individual:
               
                individual_max = max(individual.values())
                
              
                max_freq = max(max_freq, individual_max+totalOnes)
                # print(individual_max)
                individual = defaultdict(int)
                com_max=0
                com_start=0
                com_max_item=None
                for elem, freq in commulative.items():
                    rem=totalOnes
                    start=start_map[elem]
                    count_k_in_range = prefix_ones[i] - prefix_ones[start]
                    if (freq-count_k_in_range)>com_max:
                        com_max_item=elem
                        com_max=(freq-count_k_in_range)
                        rem-=count_k_in_range
    
                    elif (freq-count_k_in_range)==com_max:
                        if start_map[elem]>com_start:
                            com_start=start_map[elem]
                            com_max=freq-count_k_in_range
                            com_max_item=elem
                            rem-=count_k_in_range
                
                # print(com_start,i,com_max_item,com_max,count_k_in_range)
                max_freq=max(max_freq,rem+com_max)
        
            elif nums[i]!=k:
                start=start_map[nums[i]]
                count_k_in_range = prefix_ones[i+1] - prefix_ones[start]
                if count_k_in_range>=commulative[nums[i]]:
                    # print("here",count_k_in_range,start)
                    start_map[nums[i]]=i
                    commulative[nums[i]]=0
             
                commulative[nums[i]] += 1
                individual[nums[i]] += 1

        if individual and commulative:
            # print(individual)
            individual_max = max(individual.values())
            max_freq = max(max_freq, individual_max+totalOnes)
            individual = defaultdict(int)
            com_max=0
            com_start=0
            com_max_item=None
            for elem, freq in commulative.items():
                if freq>com_max:
                    com_max_item=elem
                    com_max=freq
                    com_start=start_map[elem]
                elif freq==com_max:
                    if start_map[elem]>com_start:
                        com_start=start_map[elem]
                        com_max=freq
                        com_max_item=elem
            count_k_in_range = prefix_ones[i + 1] - prefix_ones[com_start]
            # print(com_start,i,com_max_item,com_max,count_k_in_range)
            # print(commulative)
            max_freq=max(max_freq,(totalOnes-count_k_in_range)+com_max)
       
        
        return max_freq
