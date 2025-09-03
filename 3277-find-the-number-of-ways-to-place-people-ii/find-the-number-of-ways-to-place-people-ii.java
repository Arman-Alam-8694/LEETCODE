class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points,(a,b)->{
            if(a[0]==b[0]){
                return Integer.compare(a[1],b[1]);
            }
            return Integer.compare(b[0],a[0]);
        });
        int answers=0;
        for(int i=0;i<points.length;i++){
            int height=Integer.MAX_VALUE;
            int y=points[i][1];
            int x=points[i][0];
            for(int j=i+1;j<points.length;j++){
                int yy=points[j][1];
                if(yy>=height || y>yy){
                    continue;
                }
                answers+=1;
                height=Math.min(height,yy);
                
            }
        }
        return answers;
        
    }
}