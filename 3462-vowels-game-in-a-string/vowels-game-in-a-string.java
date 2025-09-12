class Solution {
    public boolean doesAliceWin(String s) {
        Set<Character> vowels=new HashSet<>(Arrays.asList('a','e','i','o','u'));
        for(int i=0;i<s.length();i++){
            if(vowels.contains(s.charAt(i))){
                return true;
            }
        }
        return false;


        
        
    }
}