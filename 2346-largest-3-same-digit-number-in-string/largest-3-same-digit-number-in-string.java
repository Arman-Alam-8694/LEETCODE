class Solution {
    public String largestGoodInteger(String num) {
        StringBuilder sb=new StringBuilder();
        Map<Character,Integer> map=new HashMap<>();
        int left=0;
        int elements=0;
        String maxy="";
        for(int i=0;i<num.length();i++){
            if (elements>=3){
                sb.deleteCharAt(0);
                map.put(num.charAt(left),map.get(num.charAt(left))-1);
                if(map.get(num.charAt(left))==0){
                    map.remove(num.charAt(left));
                }
                left+=1;
                elements-=1;
            }
            sb.append(num.charAt(i));
            map.put(num.charAt(i),map.getOrDefault(num.charAt(i),0)+1);
            elements+=1;
            if(elements==3 && map.keySet().size()==1){
                if(sb.toString().compareTo(maxy)>0){
                  
                    maxy=sb.toString();
                }
                
            }

        }
        return maxy;

        
    }
}