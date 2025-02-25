class Solution {
    public int numOfSubarrays(int[] arr) {
        int n=arr.length;
        System.out.println(n);
        long MOD = 1000000007; 
        long result=0;
        int evenCnts=0;
        int oddCnts=0;
        int runSum=0;
        for (int i:arr){
            runSum+=i;
            if(runSum%2!=0){
                oddCnts+=1;
                result+=evenCnts+1;
            }
            else{
                evenCnts+=1;
                result+=oddCnts;
            }
        }
        return (int)(result%MOD);
        
    }
}