class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int n=bits.length;
        int start=0;
        while(start<n-1){
            if(start+2<=n-2){
                if(bits[start]==1){
                    start+=2;
                }
                else if(bits[start+1]==1){
                    start+=3;
                }else{
                    start+=1;
                }
            }else if(start+1<=n-2){
                if(bits[start]==0){
                    if(bits[start+1]==1){
                        return false;
                    }else{
                        start+=2;
                    }
                }else{
                    start+=2;
                }
                
            }else{
                if(bits[start]==0){
                    return true;
                }
                return false;
            }
           
       
        }
        return true;
        


        
    }
}