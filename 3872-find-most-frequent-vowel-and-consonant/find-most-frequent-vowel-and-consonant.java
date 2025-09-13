class Solution {
    public int maxFreqSum(String s) {
        int vowelMax=0;
        int consMax=0;
        HashSet<Character> vowels=new HashSet<>(List.of('a','e','i','o','u'));
        HashMap<Character, Integer> v=new HashMap<>();
        HashMap<Character, Integer> c=new HashMap<>();

        for(int i=0;i<s.length();i++){
            if(vowels.contains(s.charAt(i))){
                v.put(s.charAt(i),v.getOrDefault(s.charAt(i),0)+1);
                vowelMax=Math.max(vowelMax,v.get(s.charAt(i)));

            }else{
                c.put(s.charAt(i),c.getOrDefault(s.charAt(i),0)+1);
                consMax=Math.max(consMax,c.get(s.charAt(i)));
            }
        }
        return vowelMax+consMax;

        
    }
}