class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if(numerator==0){
            return "0";
        }
        StringBuilder ans=new StringBuilder();
        if((numerator<0)^(denominator<0)){
            ans.append("-");
        }
        long num=Math.abs((long)numerator);
        long den=Math.abs((long)denominator);
        long quot=num/den;
        ans.append(quot);
        long rem=num%den;
        if(rem==0){
            return ans.toString();
        }
        Map<Long,Integer> hmap=new HashMap<>();

        ans.append(".");
        while(rem!=0){
            if(hmap.containsKey(rem)){
                int index=hmap.get(rem);
                ans.insert(index,"(");
                ans.append(")");
                break;
            }
            hmap.put(rem,ans.length());
            rem*=10;
            ans.append(rem/den);
            rem=rem%den;

        }
        return ans.toString();
    }
}