class Solution {
    public int maxFrequencyElements(int[] nums) {
        // Map<Integer,Integer> freq=new HashMap<>();
        int[] freq=new int[101];
        int max=0;
        int answer=0;
        for(int e:nums){
            int already=freq[e];
            already+=1;
            freq[e]=already;
            if(already>max){
                max=already;
                answer=0;
                answer+=max;
            }else if(already==max){
                answer+=max;

            } 
        }
        return answer;
        
    }
}