class Solution {
    public int compareVersion(String version1, String version2) {
   
        List<Integer> val=Arrays.stream(version1.split("\\.")).map(Integer::parseInt).toList();
        List<Integer> val2=Arrays.stream(version2.split("\\.")).map(Integer::parseInt).toList();
        int size=val.size()>val2.size()?val.size():val2.size();
        for(int i=0;i<size;i++){
            int first=0;
            int second=0;
            if(i<val.size()){
                first=val.get(i);
            }
            if(i<val2.size()){
                second=val2.get(i);
            }
            if(first>second){
                return 1;
            }else if(second>first){
                return -1;
            }

        }
     
        return 0;
        
    }
}