class Solution {
    public long flowerGame(int n, int m) {
        int bigger=n<m?m:n;
        int smaller=n<m?n:m;
        long even=0;
        long odd=0;
        long answer=0;
        long temp=0;
        System.out.println(bigger);
        System.out.println(smaller);
        for(int i=1;i<=bigger;i++){
            if(i<=smaller){
                if(i%2==0){
                even+=1;
            }else{
                odd+=1;
            }

            }
            
           
            if(!(i%2==0)){
                answer+=even;
                temp=even;
            }else{
                answer+=odd;
                temp=odd;
            }
            if(i<=smaller){
                answer+=temp;
                
            }
          

        }
        return answer;
        
    }
}