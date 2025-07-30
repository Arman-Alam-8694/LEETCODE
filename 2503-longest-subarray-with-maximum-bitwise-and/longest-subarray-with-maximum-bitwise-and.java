// class Solution:
//     def longestSubarray(self, nums: List[int]) -> int:
//         max_and=max(nums)
//         result=1
//         temp=0
//         for i in nums:
//             if i==max_and:
//                 temp+=1
//             else:
//                 result=max(result,temp)
//                 temp=0
//         result=max(result,temp)
//         return result
        


class Solution {
    public int longestSubarray(int[] nums) {
        int max_and=Arrays.stream(nums).max().getAsInt();
        int temp=0;
        int result=1;
        for(int i:nums){
            if(i==max_and){
                temp+=1;
            }else{
                result=Math.max(result,temp);
                temp=0;
            }
        }
        result=Math.max(result,temp);
        return result;
        
    }
}