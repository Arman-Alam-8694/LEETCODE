class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> outer =new ArrayList<>();

        outer.add(Arrays.asList(1));
        for(int i=1;i<numRows;i++){
            List<Integer> lastOne=outer.get(i-1);
            List<Integer> row=new ArrayList<>();
            row.add(1);
            for(int j=1;j<i;j++){
                row.add(lastOne.get(j-1)+lastOne.get(j));

            }
            row.add(1);
            outer.add(row);


        }
        return outer;

        
    }
}