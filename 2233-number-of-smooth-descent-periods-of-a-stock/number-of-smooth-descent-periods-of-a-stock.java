class Solution {
    public long getDescentPeriods(int[] prices) {
        long result=1;
        int left=0;
        for(int right=1;right<prices.length;right++){
            result+=1;
            if(prices[right-1]==prices[right]+1){
                result+=(right-left);
            }else{
                left=right;
            }
        }
        return result;
        
    }
}