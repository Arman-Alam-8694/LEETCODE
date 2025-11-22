class Solution {
    public int minimumOperations(int[] nums) {
        int op=0;
        for(int i:nums){
            if(!(i%3==0)){
                op+=1;
            }


        }
        return op;
        
    }
}