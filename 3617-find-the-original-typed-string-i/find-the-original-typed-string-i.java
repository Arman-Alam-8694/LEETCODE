class Solution {
    public int possibleStringCount(String word) {
        int result=1;
        int n=word.length();
        int prev=0;
        for(int i=0;i<n;i++){
            prev+=1;
            if(i==n-1 || (word.charAt(i)!=word.charAt(i+1))){
                result+=(prev-1);
                prev=0;
            }
        }
        return result;

        
    }
}