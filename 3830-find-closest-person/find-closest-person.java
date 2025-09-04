class Solution {
    public int findClosest(int x, int y, int z) {
        int aSteps=Math.abs(z-x);
        int bSteps=Math.abs(z-y);
        if(aSteps==bSteps){
            return 0;
        }else{
            return aSteps<bSteps?1:2;
        }

        
    }
}