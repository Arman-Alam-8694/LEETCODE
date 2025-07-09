// class Solution:
//     def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
//         free_space=[]
//         prev_start=0
//         for i in range(len(startTime)):
//             free_space.append(startTime[i]-prev_start)
//             prev_start=endTime[i]
//         if prev_start<eventTime:
//             free_space.append(eventTime-prev_start)
//         # print(free_space)
//         prefix_sum=[0]*len(free_space)
//         prefix_sum[0]=free_space[0]
//         for i in range(1,len(free_space)):
//             prefix_sum[i]=free_space[i]+prefix_sum[i-1]
//         # print(prefix_sum)

//         result=0
//         if len(free_space)<=k:
//             return prefix_sum[-1]
//         for i in range(0,len(free_space)-k):
//             # print(i)
//             new=prefix_sum[i+k]-(prefix_sum[i-1] if i!=0 else 0)
//             result=max(result,new)
        
//         return result
        


import java.util.*;

class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] freeSpace = new int[n + 1];  // At most n+1 gaps
        int idx = 0;
        int prev = 0;

        // Step 1: Build free space array
        for (int i = 0; i < n; i++) {
            freeSpace[idx++] = startTime[i] - prev;
            prev = endTime[i];
        }
        if (prev < eventTime) {
            freeSpace[idx++] = eventTime - prev;
        }

        // Resize freeSpace to actual length
        int[] gaps = Arrays.copyOf(freeSpace, idx);

        // Step 2: Build prefix sum array
        int[] prefixSum = new int[idx];
        prefixSum[0] = gaps[0];
        for (int i = 1; i < idx; i++) {
            prefixSum[i] = prefixSum[i - 1] + gaps[i];
        }

        // Step 3: Max free time window of size k+1
        if (idx <= k) {
            return prefixSum[idx - 1];
        }

        int result = 0;
        for (int i = 0; i + k < idx; i++) {
            int currentSum = prefixSum[i + k] - (i > 0 ? prefixSum[i - 1] : 0);
            result = Math.max(result, currentSum);
        }

        return result;
    }
}
