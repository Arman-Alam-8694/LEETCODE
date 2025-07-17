class Solution {
    public int maximumLength(int[] nums) {
        int k=2;
        int[][] dp=new int[k][k];
        int answer=0;
        for(int num:nums){
            num%=k;
            for(int i=0;i<k;i++){
                dp[num][i]=dp[i][num]+1;
                answer=Math.max(answer,dp[num][i]);
            }

        }
        return answer;
        
    }
}