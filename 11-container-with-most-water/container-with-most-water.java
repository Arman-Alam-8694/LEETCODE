class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right=height.length-1;
        int answer=0;
        while(left<right){
            if (height[left]>height[right]){
                answer=Math.max(answer,height[right]*(right-left));
                right-=1;
            }else if (height[right]>height[left]){
                answer=Math.max(answer,height[left]*(right-left));
                left+=1;
            }else{
                answer=Math.max(answer,height[left]*(right-left));
                if((right-left+1)==3){
                    break;
                }
                else if(right-1>left && left+1<right){
                    if (height[left+1]>height[right-1]){
                        left+=1;
                    }else if (height[right-1]>height[left+1]){
                        right-=1;
                        }else{
                            left+=1;
                        }


                }else{
                    break;
                }

            }
            
        }
        return answer;
       
        
    }
 
}