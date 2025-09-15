class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        // char[] chrr=brokenLetters.toCharArray();
        HashSet<Character> check=new HashSet<>();
        for(int j=0;j<brokenLetters.length();j++){
            check.add(brokenLetters.charAt(j));
        }
        int answer=0;
        int count=1;
        boolean pass=false;
        for(int i=0;i<text.length();i++){
            if(text.charAt(i)==' '){
                count+=1;
                pass=false;
                continue;
            }
            if(pass){
                continue;
            }
            if(check.contains(text.charAt(i))){
                pass=true;
                answer+=1;

            }
        }
        return count-answer;
        
    }
}