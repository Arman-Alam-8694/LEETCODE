class Solution {
    public int totalMoney(int n) {
        int cur=n;
        int sum=0;
        int times=cur/7;
        int rem=cur%7;
        int a=1;
        for(int i=0;i<times;i++){
            sum+=7*(2*a+6)/2;
            a+=1;
            
        }
        if(rem>0){
            sum+=rem*(2*a+(rem-1))/2;

        }
        return sum;

        
    }
}