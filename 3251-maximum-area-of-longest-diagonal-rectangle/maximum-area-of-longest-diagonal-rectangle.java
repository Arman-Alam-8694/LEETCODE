class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double max_diagonal=0;
        int area=0;
        for(int[] param:dimensions){
            int l=param[0];
            int b=param[1];
            double d=l*l+b*b;
            if(d>max_diagonal){
                area=l*b;
                max_diagonal=d;
            }
            else if(max_diagonal==d){
                area=Math.max(area,l*b);
            }
        }
        return area;

        
    }
}