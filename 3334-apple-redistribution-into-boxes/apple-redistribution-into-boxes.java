class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        List<Integer> c=IntStream.of(capacity).mapToObj(Integer::valueOf).sorted((a,b)->b-a).toList();
        int total=IntStream.of(apple).sum();
        int temp=0;
       
        for(int i=0;i<c.size();i++){
            temp+=c.get(i);
            if(temp>=total){
                return i+1;
            }

        }
        return c.size();


        
    }
}