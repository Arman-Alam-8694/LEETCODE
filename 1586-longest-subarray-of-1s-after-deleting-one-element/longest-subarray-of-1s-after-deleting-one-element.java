class Solution {
    public int longestSubarray(int[] nums) {
        int nleft=0;
        int left=0;
        int answer=0;
        for(int i:nums){
            if(i==0){
                answer=Math.max(answer,left+nleft);
                left=nleft;
                nleft=0;

            }else{
                nleft++;
            }
       
        }
        answer=Math.max(answer,left+nleft);
        return answer!=nums.length?answer:answer-1;
    }
}