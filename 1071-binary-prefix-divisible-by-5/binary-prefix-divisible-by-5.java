class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        int val=0;
        List<Boolean> ans=new ArrayList<>();

        for(int i=0;i<nums.length;i++){
            val=((val<<1)+nums[i])%5;
            ans.add(val==0);

        }
        return ans;
        
    }
}