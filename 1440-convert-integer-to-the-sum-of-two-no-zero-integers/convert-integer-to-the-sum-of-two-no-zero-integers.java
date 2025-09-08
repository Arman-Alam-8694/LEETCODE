class Solution {
    public int[] getNoZeroIntegers(int n) {
        int[] answer=new int[2];
        answer[0]=1;
        answer[1]=n-answer[0];
        while(check(answer[0])|check(answer[1])){
            answer[0]=answer[0]+1;
            answer[1]=n-answer[0];


        }
        return answer;
        
    }
    public boolean check(int n){
        String num=String.valueOf(n);
        for(int i=0;i<num.length();i++){
            if(num.charAt(i)=='0'){
                return true;
            }
        }
        return false;
    }
}