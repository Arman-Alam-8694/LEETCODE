class Solution {
    public boolean increasingTriplet(int[] nums) {
        int[] stack=new int[]{Integer.MAX_VALUE,Integer.MAX_VALUE,Integer.MAX_VALUE};
        System.out.println(Arrays.toString(stack));
        for(int i=0;i<nums.length;i++){
            if(stack[0]>=nums[i]){
                stack[0]=nums[i];
            }else if(stack[1]>=nums[i]){
                stack[1]=nums[i];
            }else{
                return true;
            }
        }
        return false;

        
    }
}