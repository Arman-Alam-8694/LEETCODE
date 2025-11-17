class Solution {
    public int numSub(String s) {
        int n=s.length();
        long mod=1000000007L;
        long counts=0;
        int left=-1;
        for(int right=0;right<n;right++){
            if(s.charAt(right)=='1'){
                if(left==-1){
                    left=right;
                }
                counts+=(right-left)+1;
            }else{
                left=-1;
            }
        }
        return (int)(counts%mod);
        
    }
}