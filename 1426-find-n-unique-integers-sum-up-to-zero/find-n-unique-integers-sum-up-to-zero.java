class Solution {
    public int[] sumZero(int n) {
        int[] answer=new int[n];
        int left=0;
        int right=n-1;
        int put=1;
        while(left<right){
            answer[left]=put;
            answer[right]=put*(-1);
            put+=1;
            left+=1;
            right-=1;
        }
        if(left==right){
            answer[left]=0;
        }
        return answer;

        
    }
}