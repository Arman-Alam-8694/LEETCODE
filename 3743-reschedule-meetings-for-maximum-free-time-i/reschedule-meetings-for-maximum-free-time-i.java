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
        


class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n =startTime.length;
        List<Integer> free_space=new ArrayList<>();
        int prev=0;
        for(int i=0;i<n;i++){
            free_space.add(startTime[i]-prev);
            prev=endTime[i];

        }
        if (prev<eventTime){
            free_space.add(eventTime-prev);
        }
        n =free_space.size();
        int[] prefix_sum=new int[n];
        prefix_sum[0]=free_space.get(0);
        for(int i=1;i<n;i++){
            prefix_sum[i]=prefix_sum[i-1]+free_space.get(i);
        }
        // System.out.println(free_space);
        // System.out.println(Arrays.toString(prefix_sum));
        int result=0;
        if(free_space.size()<=k){
            return prefix_sum[prefix_sum.length-1];
        }
        for(int i=0;i<prefix_sum.length-k;i++){
            int neww=prefix_sum[i+k]-(i!=0?prefix_sum[i-1]:0);
            result=Math.max(result,neww);
        }
        
        return result;


        
    }
}