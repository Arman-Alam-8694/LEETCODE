from collections import defaultdict,Counter
from typing import List



class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(set(nums))==1:
            if nums[0]==k:
                return len(nums)
        n = len(nums)
        start_map = {}
        prefix_ones = [0] * (n + 1)
        commulative = defaultdict(int)
       
        start = 0
        end = n - 1
        corners=0
        # while start < n and nums[start] == k:
        #     start += 1
        #     corners+=1
        
        # while end >= 0 and nums[end] == k:
        #     end -= 1
        #     corners+=1
    
        totalOnes=0
        for i in range(start,end+1):
            if nums[i] == k :
                prefix_ones[i+1]=prefix_ones[i]+1
                totalOnes+=1
            else:
                prefix_ones[i+1]=prefix_ones[i]
            if nums[i] not in start_map:
                start_map[nums[i]] = i

        totalOnes=totalOnes+corners
        max_freq = float('-inf')
        cumulative_max =0
        individual = defaultdict(int)
        inbetween = 0
  
        
        for i in range(start, end + 1):
            if nums[i] == k and individual:
                individual_max = max(individual.values())
                max_freq = max(max_freq, individual_max+totalOnes)
                individual = defaultdict(int)
                com_max=0
                com_start=0
                com_max_item=None
                for elem, freq in commulative.items():
                    rem=totalOnes
                    start=start_map[elem]
                    count_k_in_range = prefix_ones[i] - prefix_ones[start]
                    if (freq-count_k_in_range)>com_max:
        
                        com_max=(freq-count_k_in_range)
                        rem-=count_k_in_range

                max_freq=max(max_freq,rem+com_max)
        
            elif nums[i]!=k:
                start=start_map[nums[i]]
                count_k_in_range = prefix_ones[i+1] - prefix_ones[start]
                if count_k_in_range>=commulative[nums[i]]:
                    start_map[nums[i]]=i
                    commulative[nums[i]]=0
             
                commulative[nums[i]] += 1
                individual[nums[i]] += 1

        if individual and commulative:
            individual_max = max(individual.values())
            max_freq = max(max_freq, individual_max+totalOnes)
            individual = defaultdict(int)
            com_max=0
            com_start=0
            com_max_item=None
            for elem, freq in commulative.items():
                rem=totalOnes
                start=start_map[elem]
                count_k_in_range = prefix_ones[i+1] - prefix_ones[start]
                if (freq-count_k_in_range)>com_max:
                    com_max=(freq-count_k_in_range)
                    rem-=count_k_in_range

            max_freq=max(max_freq,rem+com_max)
        return max_freq
