class Solution {
    public boolean isPowerOfFour(int n) {
        if(n<=0){return false;}
        String bin =Integer.toBinaryString(n);
        int ones=0;
        int zeroes=0;
        for(int i=bin.length()-1;i>=0;i--){
            if(bin.charAt(i)=='0'){
                zeroes+=1;
            }
            else{
                ones+=1;
            }
        }
        if(ones==1 && (zeroes%2==0)){
            return true;
        }
        return false;
    }
}